#!/usr/bin/env python3
"""
Vissu Tours MCP Server — Model Context Protocol compatible server
Implements JSON-RPC 2.0 over stdio for AI coding agents (opencode, Claude Code, etc.)

Available MCP Tools:
  - search_tours: Search tour packages by keywords, budget, or type
  - get_recommendations: AI-powered tour recommendations via Gemini
  - book_tour: Create a booking for a tour
  - get_itinerary: Generate a day-by-day travel itinerary
"""

from __future__ import annotations
import json
import sys
import random
import string
import os
import urllib.request
import urllib.error
from typing import Any, Optional

# ---------- Tour Database ----------
TOURS = [
    {"id": 1, "name": "Backwaters Bliss", "location": "Kerala, India", "price": 24999, "duration": 5,
     "type": "Nature", "rating": 4.8, "tags": ["nature", "houseboat", "relaxing"],
     "itinerary": ["Day 1: Arrive Kochi, explore Fort Kochi", "Day 2: Drive to Alleppey, board houseboat",
                   "Day 3: Cruise backwaters, village visit", "Day 4: Kumarakom bird sanctuary",
                   "Day 5: Depart from Kochi"]},
    {"id": 2, "name": "Golden Triangle", "location": "Delhi-Agra-Jaipur", "price": 32999, "duration": 6,
     "type": "Heritage", "rating": 4.9, "tags": ["heritage", "culture", "history"],
     "itinerary": ["Day 1: Arrive Delhi, India Gate, Qutub Minar", "Day 2: Delhi sightseeing, drive to Agra",
                   "Day 3: Taj Mahal sunrise, Agra Fort", "Day 4: Drive to Jaipur via Fatehpur Sikri",
                   "Day 5: Amber Fort, Hawa Mahal, City Palace", "Day 6: Depart Jaipur"]},
    {"id": 3, "name": "Himalayan Escape", "location": "Manali-Leh, India", "price": 45999, "duration": 8,
     "type": "Adventure", "rating": 4.7, "tags": ["adventure", "mountains", "roadtrip"],
     "itinerary": ["Day 1: Arrive Manali, acclimatize", "Day 2: Manali to Jispa via Rohtang Pass",
                   "Day 3: Jispa to Sarchu", "Day 4: Sarchu to Leh via Tanglang La",
                   "Day 5: Leh local - Shanti Stupa, Leh Palace", "Day 6: Nubra Valley via Khardung La",
                   "Day 7: Pangong Lake", "Day 8: Depart Leh"]},
    {"id": 4, "name": "Goa Beach Retreat", "location": "Goa, India", "price": 18999, "duration": 4,
     "type": "Beach", "rating": 4.6, "tags": ["beach", "party", "relaxing"],
     "itinerary": ["Day 1: Arrive Goa, North Goa beaches", "Day 2: Old Goa churches, Panjim",
                   "Day 3: South Goa beaches, water sports", "Day 4: Depart from Goa"]},
    {"id": 5, "name": "Temple Trail", "location": "Tamil Nadu, India", "price": 27999, "duration": 7,
     "type": "Spiritual", "rating": 4.8, "tags": ["spiritual", "heritage", "culture"],
     "itinerary": ["Day 1: Arrive Chennai, drive to Mahabalipuram", "Day 2: Mahabalipuram shore temples",
                   "Day 3: Drive to Madurai, Meenakshi Temple", "Day 4: Madurai to Rameshwaram",
                   "Day 5: Rameshwaram to Thanjavur", "Day 6: Brihadeeswara Temple, Tanjore paintings",
                   "Day 7: Depart Trichy"]},
    {"id": 6, "name": "Island Paradise", "location": "Andaman, India", "price": 39999, "duration": 6,
     "type": "Beach", "rating": 4.9, "tags": ["island", "beach", "scuba", "nature"],
     "itinerary": ["Day 1: Arrive Port Blair, Cellular Jail", "Day 2: Havelock Island, Radhanagar Beach",
                   "Day 3: Scuba diving at Elephant Beach", "Day 4: Neil Island",
                   "Day 5: Ross Island, North Bay", "Day 6: Depart Port Blair"]},
    {"id": 7, "name": "Royal Rajasthan", "location": "Udaipur-Jodhpur-Jaisalmer", "price": 36999, "duration": 8,
     "type": "Heritage", "rating": 4.8, "tags": ["heritage", "desert", "luxury"],
     "itinerary": ["Day 1: Arrive Udaipur, City Palace, lake cruise", "Day 2: Udaipur to Jodhpur",
                   "Day 3: Mehrangarh Fort, Blue City walk", "Day 4: Jodhpur to Jaisalmer",
                   "Day 5: Jaisalmer Fort, Patwon Ki Haveli", "Day 6: Desert camp, camel safari",
                   "Day 7: Return to Jodhpur", "Day 8: Depart"]},
    {"id": 8, "name": "North East Odyssey", "location": "Meghalaya-Assam", "price": 42999, "duration": 9,
     "type": "Nature", "rating": 4.7, "tags": ["nature", "wildlife", "culture"],
     "itinerary": ["Day 1: Arrive Guwahati, Kamakhya Temple", "Day 2: Shillong - Umiam Lake, Elephant Falls",
                   "Day 3: Cherrapunji - living root bridges", "Day 4: Mawsynram, Mawlynnong",
                   "Day 5: Kaziranga National Park", "Day 6: Kaziranga elephant safari",
                   "Day 7: Majuli island", "Day 8: Guwahati", "Day 9: Depart"]},
    {"id": 9, "name": "Bali Bliss", "location": "Bali, Indonesia", "price": 54999, "duration": 7,
     "type": "International", "rating": 4.8, "tags": ["international", "beach", "culture"],
     "itinerary": ["Day 1: Arrive Bali, Seminyak", "Day 2: Ubud - rice terraces, monkey forest",
                   "Day 3: Tirta Empul temple, coffee plantation", "Day 4: Nusa Penida day trip",
                   "Day 5: Uluwatu temple, Kecak dance", "Day 6: Beach day, water sports",
                   "Day 7: Depart Bali"]},
    {"id": 10, "name": "Dubai Extravaganza", "location": "Dubai, UAE", "price": 62999, "duration": 5,
     "type": "International", "rating": 4.7, "tags": ["international", "luxury", "city"],
     "itinerary": ["Day 1: Arrive Dubai, Dubai Mall, Burj Khalifa", "Day 2: Old Dubai, Gold Souk, Abra ride",
                   "Day 3: Desert safari, BBQ dinner", "Day 4: Atlantis Aquaventure, Palm Jumeirah",
                   "Day 5: Depart"]},
    {"id": 11, "name": "Thailand Explorer", "location": "Bangkok-Phuket", "price": 44999, "duration": 7,
     "type": "International", "rating": 4.6, "tags": ["international", "beach", "culture"],
     "itinerary": ["Day 1: Arrive Bangkok, Grand Palace", "Day 2: Floating market, Wat Arun",
                   "Day 3: Fly to Phuket", "Day 4: Phi Phi island tour", "Day 5: James Bond island",
                   "Day 6: Phuket Old Town, Big Buddha", "Day 7: Depart"]},
    {"id": 12, "name": "Vietnam Discovery", "location": "Hanoi-Halong-HCMC", "price": 49999, "duration": 8,
     "type": "International", "rating": 4.7, "tags": ["international", "culture", "nature"],
     "itinerary": ["Day 1: Arrive Hanoi, Old Quarter", "Day 2: Hanoi city tour", "Day 3: Halong Bay cruise",
                   "Day 4: Halong Bay, fly to Danang", "Day 5: Hoi An ancient town", "Day 6: Fly to HCMC",
                   "Day 7: Cu Chi tunnels, War Museum", "Day 8: Depart"]},
]

BOOKINGS = {}


def generate_booking_ref():
    return "VT-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=8))


def call_gemini(prompt: str, system_prompt: str = "") -> str:
    api_key = os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        return "Error: GEMINI_API_KEY environment variable not set. Cannot generate AI recommendations."

    api_key_encoded = urllib.parse.quote(api_key, safe="")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={api_key_encoded}"

    body: Any = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}]
    }
    if system_prompt:
        body["system_instruction"] = {"parts": [{"text": system_prompt}]}

    try:
        req = urllib.request.Request(
            url,
            data=json.dumps(body).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["candidates"][0]["content"]["parts"][0]["text"]
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8") if e.fp else ""
        return f"Gemini API error ({e.code}): {error_body[:300]}"
    except Exception as e:
        return f"Error calling Gemini: {str(e)}"


# ---------- Tool Implementations ----------

def tool_search_tours(args: dict) -> str:
    keyword = args.get("keyword", "").lower()
    budget = args.get("max_budget")
    tour_type = args.get("type", "").lower()
    tags = args.get("tags", "").lower()

    results = TOURS
    if keyword:
        results = [t for t in results if keyword in t["name"].lower() or keyword in t["location"].lower()]
    if tour_type:
        results = [t for t in results if tour_type in t["type"].lower()]
    if tags:
        tag_list = [tag.strip().lower() for tag in tags.split(",")]
        results = [t for t in results if any(tag in t["tags"] for tag in tag_list)]
    if budget:
        results = [t for t in results if t["price"] <= budget]

    if not results:
        return "No tours found matching your criteria."

    out = [f"Found {len(results)} tours:"]
    for t in results:
        out.append(f"  [{t['id']}] {t['name']} — {t['location']}")
        out.append(f"      Price: ₹{t['price']:,} | Duration: {t['duration']} days | Rating: {t['rating']}/5")
        out.append(f"      Type: {t['type']} | Tags: {', '.join(t['tags'])}")
        out.append(f"      Itinerary: {' > '.join(t['itinerary'])}")
        out.append("")
    return "\n".join(out)


def tool_get_recommendations(args: dict) -> str:
    preferences = args.get("preferences", "")
    budget = args.get("budget", "")
    travelers = args.get("travelers", "2")
    duration = args.get("duration", "")

    tour_summary = "\n".join([
        f"- {t['name']} ({t['location']}): {t['type']} tour, {t['duration']} days, ₹{t['price']:,}, "
        f"Rating {t['rating']}/5, Tags: {', '.join(t['tags'])}"
        for t in TOURS
    ])

    prompt = f"""A traveler is looking for tour recommendations with the following preferences:
- Preferences: {preferences}
- Budget: {budget}
- Travelers: {travelers}
- Duration: {duration}

Here are the available tours from Vissu Tours:
{tour_summary}

Recommend the top 3 tours matching their preferences. For each recommendation, explain WHY it matches.
Also provide 2-3 travel tips relevant to their preferences. Be enthusiastic and friendly."""

    system = "You are Visu, the AI travel assistant for Vissu Tours. You are friendly, knowledgeable about Indian and international travel, and give concise but helpful recommendations."

    return call_gemini(prompt, system)


def tool_book_tour(args: dict) -> str:
    tour_id = args.get("tour_id")
    traveler_name = args.get("name", "Anonymous")
    email = args.get("email", "")
    date = args.get("date", "Not specified")
    guests = args.get("guests", 2)

    tour = next((t for t in TOURS if t["id"] == tour_id), None)
    if not tour:
        return f"Error: No tour found with ID {tour_id}"

    ref = generate_booking_ref()
    BOOKINGS[ref] = {
        "tour": tour["name"],
        "location": tour["location"],
        "price": tour["price"],
        "traveler": traveler_name,
        "email": email,
        "date": date,
        "guests": guests,
        "total": tour["price"] * int(guests),
        "status": "confirmed"
    }

    return json.dumps({
        "status": "confirmed",
        "booking_ref": ref,
        "tour": tour["name"],
        "location": tour["location"],
        "price_per_person": tour["price"],
        "guests": guests,
        "total_amount": tour["price"] * int(guests),
        "date": date,
        "message": f"Booking confirmed! Your reference is {ref}. Check your email ({email}) for details."
    }, indent=2)


def tool_get_itinerary(args: dict) -> str:
    tour_id = args.get("tour_id")
    custom_prefs = args.get("customizations", "")

    tour = next((t for t in TOURS if t["id"] == tour_id), None)
    if not tour:
        return f"Error: No tour found with ID {tour_id}"

    base_itinerary = "\n".join(tour["itinerary"])

    if not custom_prefs:
        return f"Itinerary for {tour['name']} ({tour['location']}):\n{base_itinerary}\n\nDuration: {tour['duration']} days | Price: ₹{tour['price']:,} per person"

    prompt = f"""Base itinerary for {tour['name']} ({tour['location']}, {tour['duration']} days):
{base_itinerary}

The traveler wants these customizations: {custom_prefs}

Suggest modifications to the itinerary that incorporate their requests while still covering the key highlights. Be specific about what to change per day."""

    system = "You are Visu, the AI travel planner. You specialize in customizing itineraries for Indian and international tours."

    ai_response = call_gemini(prompt, system)
    return f"""Original itinerary for {tour['name']}:
{base_itinerary}

--- AI-Customized Suggestions ---
{ai_response}
"""


# ---------- MCP JSON-RPC 2.0 Server ----------

TOOLS = {
    "search_tours": {
        "description": "Search Vissu Tours packages by keyword, budget, type, or tags",
        "schema": {
            "type": "object",
            "properties": {
                "keyword": {"type": "string", "description": "Search keyword for tour name or location"},
                "max_budget": {"type": "number", "description": "Maximum budget in INR"},
                "type": {"type": "string", "description": "Tour type: Nature, Heritage, Adventure, Beach, Spiritual, International"},
                "tags": {"type": "string", "description": "Comma-separated tags: nature, beach, adventure, heritage, luxury, etc."}
            }
        }
    },
    "get_recommendations": {
        "description": "Get AI-powered tour recommendations from Visu (uses Gemini LLM)",
        "schema": {
            "type": "object",
            "properties": {
                "preferences": {"type": "string", "description": "Travel preferences: interests, style, must-haves"},
                "budget": {"type": "string", "description": "Budget range description"},
                "travelers": {"type": "string", "description": "Number of travelers"},
                "duration": {"type": "string", "description": "Preferred trip duration"}
            }
        }
    },
    "book_tour": {
        "description": "Book a tour package from Vissu Tours",
        "schema": {
            "type": "object",
            "properties": {
                "tour_id": {"type": "number", "description": "Tour ID from search results"},
                "name": {"type": "string", "description": "Traveler's full name"},
                "email": {"type": "string", "description": "Email address"},
                "date": {"type": "string", "description": "Preferred travel date (YYYY-MM-DD)"},
                "guests": {"type": "number", "description": "Number of travelers (default: 2)"}
            },
            "required": ["tour_id", "name", "email"]
        }
    },
    "get_itinerary": {
        "description": "Get or customize a day-by-day itinerary for a specific tour",
        "schema": {
            "type": "object",
            "properties": {
                "tour_id": {"type": "number", "description": "Tour ID to get itinerary for"},
                "customizations": {"type": "string", "description": "Optional: custom requests for the itinerary"}
            },
            "required": ["tour_id"]
        }
    },
    "list_tours": {
        "description": "List all available tour packages from Vissu Tours",
        "schema": {
            "type": "object",
            "properties": {}
        }
    }
}

TOOL_FUNCTIONS = {
    "search_tours": tool_search_tours,
    "get_recommendations": tool_get_recommendations,
    "book_tour": tool_book_tour,
    "get_itinerary": tool_get_itinerary,
    "list_tours": lambda args: tool_search_tours({}),
}


def handle_request(req: dict) -> Optional[dict]:
    """Process a single JSON-RPC 2.0 request and return a response."""
    req_id = req.get("id")
    method = req.get("method", "")

    # --- Initialize ---
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "serverInfo": {
                    "name": "vissu-tours-mcp",
                    "version": "1.0.0"
                },
                "capabilities": {
                    "tools": {}
                }
            }
        }

    # --- Initialized notification ---
    if method == "notifications/initialized":
        return None

    # --- Tools List ---
    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": name,
                        "description": info["description"],
                        "inputSchema": info["schema"]
                    }
                    for name, info in TOOLS.items()
                ]
            }
        }

    # --- Tools Call ---
    if method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name", "")
        arguments = params.get("arguments", {})

        if tool_name not in TOOL_FUNCTIONS:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Unknown tool: {tool_name}"}
            }

        try:
            result_text = TOOL_FUNCTIONS[tool_name](arguments)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {"type": "text", "text": result_text}
                    ]
                }
            }
        except Exception as e:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32000, "message": f"Tool error: {str(e)}"}
            }

    # --- Resources List ---
    if method == "resources/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "resources": [
                    {"uri": "vissu://tours", "name": "All Tour Packages", "mimeType": "application/json"},
                    {"uri": "vissu://bookings", "name": "Current Bookings", "mimeType": "application/json"}
                ]
            }
        }

    # --- Resources Read ---
    if method == "resources/read":
        uri = req.get("params", {}).get("uri", "")
        if uri == "vissu://tours":
            content = json.dumps(TOURS, indent=2)
        elif uri == "vissu://bookings":
            content = json.dumps(BOOKINGS, indent=2)
        else:
            return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32602, "message": f"Unknown resource: {uri}"}}
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"contents": [{"uri": uri, "mimeType": "application/json", "text": content}]}
        }

    # --- Ping ---
    if method == "ping":
        return {"jsonrpc": "2.0", "id": req_id, "result": {}}

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32601, "message": f"Method not found: {method}"}
    }


def main():
    """Run the MCP server: JSON-RPC 2.0 over stdin/stdout."""
    import argparse
    p = argparse.ArgumentParser(description="Vissu Tours MCP Server")
    p.add_argument("--test", action="store_true", help="Run in test mode (interactive)")
    args = p.parse_args()

    if args.test:
        print("Vissu Tours MCP Server — Test Mode", file=sys.stderr)
        print("Type JSON-RPC requests. Examples:", file=sys.stderr)
        print('  {"jsonrpc":"2.0","method":"initialize","id":1}', file=sys.stderr)
        print('  {"jsonrpc":"2.0","method":"tools/list","id":2}', file=sys.stderr)
        print('  {"jsonrpc":"2.0","method":"tools/call","params":{"name":"search_tours","arguments":{"keyword":"kerala"}},"id":3}', file=sys.stderr)
        print('  {"jsonrpc":"2.0","method":"tools/call","params":{"name":"get_recommendations","arguments":{"preferences":"beach vacation with family, moderate budget"}},"id":4}', file=sys.stderr)
        print(file=sys.stderr)

        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                req = json.loads(line)
                resp = handle_request(req)
                if resp is not None:
                    print(json.dumps(resp))
            except json.JSONDecodeError as e:
                print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": f"Parse error: {e}"}}))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                req = json.loads(line)
                resp = handle_request(req)
                if resp is not None:
                    sys.stdout.write(json.dumps(resp) + "\n")
                    sys.stdout.flush()
            except json.JSONDecodeError:
                err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
                sys.stdout.write(json.dumps(err) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
