#!/usr/bin/env python3
"""
Vissu Tours Backend Server — Google Sheets-powered CMS
  /api/tours   → Fetches tour data from a published Google Sheet (CSV)
  /api/chat    → Proxies Gemini AI (API key stays server-side)
  /api/book    → Booking endpoint
  Everything else → serves static files (index.html, etc.)

Usage:
  export GEMINI_API_KEY=your_key
  export GOOGLE_SHEET_CSV_URL=https://docs.google.com/spreadsheets/d/e/.../pub?output=csv
  python3 server.py
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
import csv
import io
import time

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
GOOGLE_SHEET_URL = os.environ.get("GOOGLE_SHEET_CSV_URL", "")
PORT = int(os.environ.get("PORT", "8000"))
DIR = os.path.dirname(os.path.abspath(__file__))

# Simple in-memory cache for Google Sheets data
_cache = {"data": None, "ts": 0, "ttl": 60}  # 60 sec cache


def fetch_tours_from_sheet():
    """Fetch and parse the published Google Sheet CSV, return list of tours."""
    global _cache
    now = time.time()
    if _cache["data"] is not None and (now - _cache["ts"]) < _cache["ttl"]:
        return _cache["data"]

    if not GOOGLE_SHEET_URL:
        return None

    try:
        req = urllib.request.Request(GOOGLE_SHEET_URL)
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8")

        reader = csv.DictReader(io.StringIO(raw))
        tours = []
        for row in reader:
            try:
                tours.append({
                    "id": int(row.get("id", 0)),
                    "name": row.get("name", "").strip(),
                    "location": row.get("location", "").strip(),
                    "price": int(row.get("price", 0)),
                    "duration": row.get("duration", "").strip(),
                    "type": row.get("type", "").strip(),
                    "tags": [t.strip() for t in row.get("tags", "").split(",") if t.strip()],
                    "desc": row.get("desc", "").strip(),
                    "emoji": row.get("emoji", "🌍").strip(),
                    "color": row.get("color", "#6366f1").strip(),
                })
            except (ValueError, KeyError) as e:
                print(f"[VissuTours] Skipping row: {e}", file=sys.stderr)
                continue

        if tours:
            _cache = {"data": tours, "ts": now, "ttl": 60}
            print(f"[VissuTours] ✅ Loaded {len(tours)} tours from Google Sheet", file=sys.stderr)
            return tours
        return None
    except Exception as e:
        print(f"[VissuTours] ⚠️ Failed to fetch Google Sheet: {e}", file=sys.stderr)
        return _cache["data"]  # return stale cache if available


# Hardcoded fallback tours (used when no Google Sheet is configured)
FALLBACK_TOURS = [
    {"id":1,"name":"Backwaters Bliss","location":"Kerala, India","price":24999,"duration":"5 Days","type":"Nature","tags":["Nature","Houseboat"],"desc":"Cruise the serene backwaters of Alleppey on a luxury houseboat.","emoji":"🛶","color":"#06b6d4"},
    {"id":2,"name":"Golden Triangle","location":"Delhi-Agra-Jaipur","price":32999,"duration":"6 Days","type":"Heritage","tags":["Heritage","Culture"],"desc":"Explore India's iconic heritage circuit with guided tours.","emoji":"🏛️","color":"#f59e0b"},
    {"id":3,"name":"Himalayan Escape","location":"Manali-Leh, India","price":45999,"duration":"8 Days","type":"Adventure","tags":["Adventure","Mountains"],"desc":"Epic road trip through the Himalayas with camping & rafting.","emoji":"🏔️","color":"#8b5cf6"},
    {"id":4,"name":"Goa Beach Retreat","location":"Goa, India","price":18999,"duration":"4 Days","type":"Beach","tags":["Beach","Party"],"desc":"Sun, sand, and susegad. Best beaches & nightlife experience.","emoji":"🏖️","color":"#ec4899"},
    {"id":5,"name":"Temple Trail","location":"Tamil Nadu, India","price":27999,"duration":"7 Days","type":"Heritage","tags":["Spiritual","Heritage"],"desc":"Visit ancient Dravidian temples across Madurai, Tanjore & Rameshwaram.","emoji":"🛕","color":"#f97316"},
    {"id":6,"name":"Island Paradise","location":"Andaman, India","price":39999,"duration":"6 Days","type":"Beach","tags":["Island","Scuba"],"desc":"Crystal clear waters, coral reefs, and pristine white beaches.","emoji":"🏝️","color":"#14b8a6"},
    {"id":7,"name":"Royal Rajasthan","location":"Udaipur-Jodhpur-Jaisalmer","price":36999,"duration":"8 Days","type":"Heritage","tags":["Royal","Desert"],"desc":"Live like royalty in palaces, camel safaris in the Thar desert.","emoji":"🐪","color":"#eab308"},
    {"id":8,"name":"North East Odyssey","location":"Meghalaya-Assam","price":42999,"duration":"9 Days","type":"Nature","tags":["Nature","Culture"],"desc":"Living root bridges, Kaziranga wildlife, and tea gardens.","emoji":"🌿","color":"#22c55e"},
    {"id":9,"name":"Bali Bliss","location":"Bali, Indonesia","price":54999,"duration":"7 Days","type":"International","tags":["International","Tropical"],"desc":"Temples, rice terraces, and stunning beaches of Bali.","emoji":"🌴","color":"#06b6d4"},
    {"id":10,"name":"Dubai Extravaganza","location":"Dubai, UAE","price":62999,"duration":"5 Days","type":"International","tags":["International","Luxury"],"desc":"Burj Khalifa, desert safari, and world-class shopping.","emoji":"✨","color":"#d4a853"},
    {"id":11,"name":"Thailand Explorer","location":"Bangkok-Phuket","price":44999,"duration":"7 Days","type":"International","tags":["International","Beach"],"desc":"Floating markets, island hopping, and vibrant nightlife.","emoji":"🏯","color":"#ef4444"},
    {"id":12,"name":"Vietnam Discovery","location":"Hanoi-Halong-HCMC","price":49999,"duration":"8 Days","type":"International","tags":["International","Culture"],"desc":"Halong Bay cruise, ancient towns, and amazing street food.","emoji":"🍜","color":"#10b981"},
]


def get_tours():
    tours = fetch_tours_from_sheet()
    if tours:
        return tours
    print("[VissuTours] Using fallback tour data (no Google Sheet configured)", file=sys.stderr)
    return FALLBACK_TOURS


class VissuHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        if self.path == "/api/tours":
            try:
                tours = get_tours()
                self.send_json(200, {"tours": tours, "source": "google-sheet" if GOOGLE_SHEET_URL else "fallback"})
            except Exception as e:
                self.send_json(500, {"error": str(e)})
        elif self.path == "/health":
            self.send_json(200, {"status": "ok", "gemini": bool(GEMINI_API_KEY), "sheets": bool(GOOGLE_SHEET_URL)})
        else:
            super().do_GET()

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

        if not msg:
            self.send_json(400, {"error": "Missing 'message' field"})
            return

        # Build tour context from live data (Google Sheet or fallback)
        tours = get_tours()
        tour_context = "\n".join([
            f"- {t['name']} ({t['location']}): {t['desc']} — {t['duration']}, ₹{t['price']:,}, Tags: {', '.join(t['tags'])}"
            for t in tours
        ])

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
        resp = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(resp)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(resp)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, fmt, *args):
        print(f"[VissuTours] {args[0]}", file=sys.stderr)


class ThreadedServer(socketserver.ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    print("=" * 50, file=sys.stderr)
    print("  🧳  Vissu Tours Backend Server", file=sys.stderr)
    print("=" * 50, file=sys.stderr)

    if not GEMINI_API_KEY:
        print("⚠️  GEMINI_API_KEY not set. AI chat will be unavailable.", file=sys.stderr)
    else:
        print(f"✅ Gemini API key loaded ({GEMINI_API_KEY[:8]}...)", file=sys.stderr)

    if not GOOGLE_SHEET_URL:
        print("💡 GOOGLE_SHEET_CSV_URL not set. Using built-in tour data.", file=sys.stderr)
        print("   Set it to your published Google Sheet CSV URL for live updates.", file=sys.stderr)
    else:
        print(f"📊 Google Sheet URL configured", file=sys.stderr)
        fetch_tours_from_sheet()

    server = ThreadedServer(("0.0.0.0", PORT), VissuHandler)
    print(f"🚀 Server running at http://localhost:{PORT}", file=sys.stderr)
    print(f"   Endpoints: /api/tours | /api/chat | /api/book | /health", file=sys.stderr)
    print("   Press Ctrl+C to stop", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped", file=sys.stderr)
        server.shutdown()


if __name__ == "__main__":
    main()
