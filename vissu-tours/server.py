#!/usr/bin/env python3
"""
Vissu Tours Backend Server
Serves static files AND proxies Gemini API calls (API key stays server-side)
Usage: GEMINI_API_KEY=your_key python3 server.py
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import urllib.request
import urllib.error
import urllib.parse
import socketserver
import sys
import traceback

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
PORT = int(os.environ.get("PORT", "8000"))
DIR = os.path.dirname(os.path.abspath(__file__))


class VissuHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_POST(self):
        try:
            if self.path == "/api/chat":
                self.handle_chat()
            elif self.path == "/api/book":
                self.handle_booking()
            else:
                self.send_error(404)
        except Exception as e:
            print(f"[VissuTours] POST error: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            try:
                self.send_json(500, {"error": str(e)})
            except:
                pass

    def handle_chat(self):
        if not GEMINI_API_KEY:
            self.send_json(500, {"error": "GEMINI_API_KEY not configured on server"})
            return

        cl = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(cl))
        msg = body.get("message", "")
        tour_context = body.get("tour_context", "")

        if not msg:
            self.send_json(400, {"error": "Missing 'message' field"})
            return

        system_prompt = (
            "You are Visu, the AI travel assistant for Vissu Tours. "
            "Be friendly, enthusiastic, and helpful. "
            "You know about these tours:\n" + tour_context + "\n\n"
            "Help users with: tour recommendations, itinerary planning, "
            "budget tips, best time to visit, packing suggestions. "
            "Keep responses concise (2-4 paragraphs). Use emojis occasionally. "
            "Recommend specific tours by name when relevant."
        )

        try:
            enc_key = urllib.parse.quote(GEMINI_API_KEY, safe="")
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={enc_key}"
            req_body = {
                "system_instruction": {"parts": [{"text": system_prompt}]},
                "contents": [{"role": "user", "parts": [{"text": msg}]}]
            }
            req = urllib.request.Request(
                url,
                data=json.dumps(req_body).encode(),
                headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
            reply = data["candidates"][0]["content"]["parts"][0]["text"]
            self.send_json(200, {"reply": reply})
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8")[:500] if e.fp else ""
            print(f"[VissuTours] Gemini HTTP error {e.code}: {err}", file=sys.stderr)
            self.send_json(e.code, {"error": f"Gemini API error: {err}"})
        except Exception as e:
            print(f"[VissuTours] Chat error: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            self.send_json(500, {"error": str(e)})

    def handle_booking(self):
        cl = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(cl))
        print(f"[Booking] {body.get('tour')} — {body.get('name')} ({body.get('email')})", file=sys.stderr)
        self.send_json(200, {"status": "ok", "ref": "VT-" + "".join(
            __import__("random").choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8)
        )})

    def send_json(self, code, data):
        resp = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(resp)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(resp)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, fmt, *args):
        print(f"[VissuTours] {args[0]}", file=sys.stderr)


class ThreadedServer(socketserver.ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    if not GEMINI_API_KEY:
        print("⚠️  GEMINI_API_KEY not set. AI chat will be unavailable.", file=sys.stderr)
        print("   Set it: export GEMINI_API_KEY=your_key_here", file=sys.stderr)
    else:
        print(f"✅ Gemini API key loaded ({GEMINI_API_KEY[:8]}...)", file=sys.stderr)

    server = ThreadedServer(("0.0.0.0", PORT), VissuHandler)
    print(f"🚀 Vissu Tours server running at http://localhost:{PORT}", file=sys.stderr)
    print("   Press Ctrl+C to stop", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped", file=sys.stderr)
        server.shutdown()


if __name__ == "__main__":
    main()
