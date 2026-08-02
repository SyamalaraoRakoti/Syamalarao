#!/usr/bin/env python3
"""
Atlantic Coast Tours — Customer Engagement Chatbot Backend
Assignment: CA2 Individual — Build It Live, Prove It's Real
Business: Atlantic Coast Tours (west of Ireland travel)
Live Data: Google Sheet (assigned) + Open-Meteo Weather API
LLM Brain: Google Gemini

Endpoints:
  GET  /api/tours    — Fetch live tour data from the assigned Google Sheet
  GET  /api/weather?location=Galway  — Live weather from Open-Meteo
  POST /api/chat     — AI chatbot with Gemini, live sheet data, and weather
  GET  /health       — Health check
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

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
PORT = int(os.environ.get("PORT", "8000"))
DIR = os.path.dirname(os.path.abspath(__file__))

# Assigned Google Sheet — NO caching, fetch live every time
ASSIGNED_SHEET_URL = os.environ.get("GOOGLE_SHEET_CSV_URL",
    "https://docs.google.com/spreadsheets/d/1balBGf8QhZ5dc-RCCAPt2kcrcf6m_YRh0HL_r8bBtJw/export?format=csv")


def fetch_tours_live():
    """Fetch tours from the assigned Google Sheet — live every call, no caching."""
    try:
        req = urllib.request.Request(ASSIGNED_SHEET_URL)
        with urllib.request.urlopen(req, timeout=15) as resp:
            raw = resp.read().decode("utf-8")

        reader = csv.DictReader(io.StringIO(raw))
        tours = []
        for row in reader:
            try:
                tours.append({
                    "tour_id": row.get("tour_id", "").strip(),
                    "tour_name": row.get("tour_name", "").strip(),
                    "category": row.get("category", "").strip(),
                    "location": row.get("location", "").strip(),
                    "meeting_point": row.get("meeting_point", "").strip(),
                    "price_eur": row.get("price_eur", "").strip(),
                    "duration_hours": row.get("duration_hours", "").strip(),
                    "capacity": row.get("capacity", "").strip(),
                    "availability": row.get("availability", "").strip(),
                    "slots_this_week": row.get("slots_this_week", "").strip(),
                    "special_offer": row.get("special_offer", "").strip(),
                    "description": row.get("description", "").strip(),
                })
            except Exception as e:
                print(f"[ACT] Skipping malformed row: {e}", file=sys.stderr)
                continue
        print(f"[ACT] ✅ Fetched {len(tours)} tours live from Google Sheet", file=sys.stderr)
        return tours
    except Exception as e:
        print(f"[ACT] ⚠️ Sheet fetch error: {e}", file=sys.stderr)
        return None


# Simple in-memory cache for weather (avoid Open-Meteo rate limits on shared Render IP)
_weather_cache = {}  # {location: {"data": ..., "ts": timestamp}}


def fetch_weather(location):
    """Fetch live weather from Open-Meteo with 5-min cache per location."""
    global _weather_cache
    now = time.time()
    key = location.lower().strip()
    if key in _weather_cache and (now - _weather_cache[key]["ts"]) < 300:
        return _weather_cache[key]["data"]
    coords = {
        "galway": (53.2707, -9.0568),
        "doolin": (53.0238, -9.3777),
        "clifden": (53.4894, -10.0208),
        "westport": (53.8001, -9.5222),
        "achill": (53.9646, -10.0045),
        "ballina": (54.1145, -9.1529),
        "sligo": (54.2766, -8.4761),
        "donegal": (54.6538, -8.1094),
        "clare": (52.8402, -9.0018),
        "mayo": (53.9007, -9.2964),
        "connemara": (53.5411, -9.8833),
    }
    key = location.lower().strip()
    for k, (lat, lon) in coords.items():
        if k in key:
            break
    else:
        lat, lon = 53.2707, -9.0568  # default to Galway

    try:
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&current=temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m,wind_direction_10m"
            f"&daily=temperature_2m_max,temperature_2m_min,weather_code,precipitation_sum"
            f"&timezone=Europe/Dublin&forecast_days=3"
        )
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "AtlanticCoastTours/1.0"}), timeout=10) as resp:
            data = json.loads(resp.read().decode())

        weather_codes = {
            0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
            45: "Fog", 48: "Depositing rime fog", 51: "Light drizzle",
            53: "Moderate drizzle", 55: "Dense drizzle", 61: "Slight rain",
            63: "Moderate rain", 65: "Heavy rain", 71: "Slight snow",
            73: "Moderate snow", 75: "Heavy snow", 80: "Slight rain showers",
            81: "Moderate rain showers", 82: "Violent rain showers",
            95: "Thunderstorm", 96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail",
        }

        current = data.get("current", {})
        daily = data.get("daily", {})

        forecast_days = []
        for i in range(min(3, len(daily.get("time", [])))):
            fc = {
                "date": daily["time"][i],
                "temp_max": daily.get("temperature_2m_max", [None])[i],
                "temp_min": daily.get("temperature_2m_min", [None])[i],
                "condition": weather_codes.get(daily.get("weather_code", [0])[i], "Unknown"),
                "rain_mm": daily.get("precipitation_sum", [0])[i],
            }
            forecast_days.append(fc)

        result = {
            "location": location.title(),
            "coordinates": f"{lat}, {lon}",
            "current": {
                "temperature_c": current.get("temperature_2m"),
                "humidity_pct": current.get("relative_humidity_2m"),
                "condition": weather_codes.get(current.get("weather_code", 0), "Unknown"),
                "wind_speed_kmh": current.get("wind_speed_10m"),
                "wind_direction": current.get("wind_direction_10m"),
            },
            "forecast": forecast_days,
        }
        _weather_cache[key] = {"data": result, "ts": now}
        return result
    except Exception as e:
        print(f"[ACT] Weather error: {e}", file=sys.stderr)
        return {"error": f"Weather fetch failed: {e}", "location": location}


class ACTHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def do_GET(self):
        if self.path.startswith("/api/weather"):
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            location = params.get("location", ["Galway"])[0]
            try:
                weather = fetch_weather(location)
                if "error" in weather:
                    self.send_json(502, {"error": weather["error"], "weather": weather})
                else:
                    self.send_json(200, {"weather": weather})
            except Exception as e:
                self.send_json(500, {"error": str(e)})
        elif self.path == "/api/tours":
            try:
                tours = fetch_tours_live()
                if tours is None:
                    self.send_json(502, {"error": "Failed to fetch live sheet data"})
                else:
                    self.send_json(200, {"tours": tours, "source": "live-google-sheet"})
            except Exception as e:
                self.send_json(500, {"error": str(e)})
        elif self.path == "/health":
            self.send_json(200, {"status": "ok", "gemini_configured": bool(GEMINI_API_KEY)})
        else:
            super().do_GET()

    def do_POST(self):
        try:
            if self.path == "/api/chat":
                self.handle_chat()
            elif self.path == "/api/weather-query":
                self.handle_weather_chat()
            else:
                self.send_error(404)
        except Exception as e:
            print(f"[ACT] POST error: {e}", file=sys.stderr)
            try:
                self.send_json(500, {"error": str(e)})
            except:
                pass

    def handle_chat(self):
        if not GEMINI_API_KEY:
            self.send_json(500, {"error": "Server LLM key not configured"})
            return

        cl = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(cl))
        msg = body.get("message", "")

        if not msg:
            self.send_json(400, {"error": "Empty message"})
            return

        tours = fetch_tours_live()
        if not tours:
            self.send_json(502, {"error": "Cannot access live tour data right now"})
            return

        tour_text = []
        for t in tours:
            slots = t.get("slots_this_week", "?")
            price = t.get("price_eur", "?")
            special = f" — OFFER: {t['special_offer']}" if t.get("special_offer") else ""
            avail = f" (availability: {t['availability']}, {slots} slots this week)" if slots != "?" else ""
            tour_text.append(
                f"- {t['tour_id']}: {t['tour_name']} | {t['category']} | "
                f"{t['location']} | €{price} | {t['duration_hours']}hrs "
                f"| Capacity: {t['capacity']}{avail}{special}"
            )

        # System prompt that teaches the bot to report sheet data faithfully
        system_prompt = (
            "You are Seamus, the friendly customer-support chatbot for Atlantic Coast Tours, "
            "a tour company operating along the Wild Atlantic Way in the west of Ireland. "
            "You help customers find tours, check prices, availability, and weather conditions. "
            "Keep responses warm, helpful, and concise (2-4 paragraphs). Use occasional Irish charm.\n\n"
            "CRITICAL RULES:\n"
            "1. ALWAYS report prices exactly as they appear in the live tour data below. "
            "If a price looks absurd (e.g., millions of euros), report it faithfully — "
            "do not correct, 'fix', or invent a different price. State it and note if it seems unusual.\n"
            "2. If a tour shows 0 slots available, tell the customer honestly.\n"
            "3. When asked about weather, recommend checking the live weather tool "
            "(tell the customer you can look up the forecast if they tell you which location).\n"
            "4. Mention special offers when relevant.\n"
            "5. Do not invent tour data — if something isn't in the sheet, say you don't have that info.\n\n"
            "LIVE TOUR DATA FROM GOOGLE SHEET (fetched right now):\n" + "\n".join(tour_text)
        )

        try:
            enc_key = urllib.parse.quote(GEMINI_API_KEY, safe="")
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={enc_key}"
            req_body = {
                "system_instruction": {"parts": [{"text": system_prompt}]},
                "contents": [{"role": "user", "parts": [{"text": msg}]}]
            }
            req = urllib.request.Request(
                url, data=json.dumps(req_body).encode(), headers={"Content-Type": "application/json"}
            )
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode())
            reply = data["candidates"][0]["content"]["parts"][0]["text"]
            self.send_json(200, {"reply": reply, "data_source": "live-sheet"})
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8")[:500] if e.fp else ""
            self.send_json(e.code, {"error": f"LLM error: {err}"})
        except Exception as e:
            self.send_json(500, {"error": str(e)})

    def handle_weather_chat(self):
        """Combined weather + chat endpoint for bonus: sheet + weather in one reply."""
        cl = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(cl))
        location = body.get("location", "Galway")

        weather = fetch_weather(location)
        if "error" in weather:
            self.send_json(200, {"weather": weather})
            return

        # Build a combined reply using Gemini if key is available
        if GEMINI_API_KEY:
            tours = fetch_tours_live()
            tour_locations = set()
            for t in (tours or []):
                if location.lower() in t.get("location", "").lower():
                    tour_locations.add(t["tour_name"])

            w = weather["current"]
            fc = weather["forecast"]
            fc_text = "\n".join(
                [f"  {d['date']}: {d['condition']}, {d['temp_min']}–{d['temp_max']}°C, Rain: {d['rain_mm']}mm"
                 for d in fc]
            )

            ctx = (
                f"Weather for {location} right now: {w['temperature_c']}°C, "
                f"{w['condition']}, Humidity: {w['humidity_pct']}%, Wind: {w['wind_speed_kmh']}km/h\n"
                f"3-day forecast:\n{fc_text}\n"
            )
            if tour_locations:
                ctx += f"Tours in this area: {', '.join(tour_locations)}"

            try:
                enc_key = urllib.parse.quote(GEMINI_API_KEY, safe="")
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={enc_key}"
                prompt = (
                    f"Here is live weather data for {location}, Ireland:\n{ctx}\n\n"
                    f"Write a friendly, one-paragraph weather update for a customer of "
                    f"Atlantic Coast Tours. If there are tours in the area, mention them. "
                    f"Advise if the weather is good for outdoor activities."
                )
                req_body = {
                    "contents": [{"role": "user", "parts": [{"text": prompt}]}]
                }
                req = urllib.request.Request(
                    url, data=json.dumps(req_body).encode(),
                    headers={"Content-Type": "application/json"}
                )
                with urllib.request.urlopen(req, timeout=15) as resp:
                    data = json.loads(resp.read().decode())
                summary = data["candidates"][0]["content"]["parts"][0]["text"]
                self.send_json(200, {"weather": weather, "summary": summary})
            except:
                self.send_json(200, {"weather": weather, "summary": f"Current: {w['temperature_c']}°C, {w['condition']}"})
        else:
            self.send_json(200, {"weather": weather})

    def send_json(self, code, data):
        resp = json.dumps(data, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(resp)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()
        self.wfile.write(resp)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, fmt, *args):
        print(f"[ACT] {args[0]}", file=sys.stderr)


class ThreadedServer(socketserver.ThreadingMixIn, HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


def main():
    print("=" * 55, file=sys.stderr)
    print("  🌊  Atlantic Coast Tours — Customer Chatbot", file=sys.stderr)
    print("  📊 Live Sheet: Atlantic Coast Tours (assigned)", file=sys.stderr)
    print("  🌤️  Weather: Open-Meteo (live)", file=sys.stderr)
    print("=" * 55, file=sys.stderr)

    if not GEMINI_API_KEY:
        print("⚠️  GEMINI_API_KEY not set. Chat will not work.", file=sys.stderr)
    else:
        print(f"✅ LLM brain ready ({GEMINI_API_KEY[:8]}...)", file=sys.stderr)

    server = ThreadedServer(("0.0.0.0", PORT), ACTHandler)
    print(f"🚀 Server: http://localhost:{PORT}", file=sys.stderr)
    print(f"   /api/tours | /api/weather?location=Galway | /api/chat", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped", file=sys.stderr)


if __name__ == "__main__":
    main()
