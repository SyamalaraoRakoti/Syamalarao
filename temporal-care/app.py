import os
from flask import Flask, request, jsonify
from google import genai
import time

app = Flask(__name__)

# Configure your API Key (Set this as an environment variable)
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Basic rate limiting (15 requests/minute = 4 seconds per request)
last_request_time = 0
MIN_INTERVAL = 4

@app.route('/chat', methods=['POST'])
def chat():
    global last_request_time
    
    # Simple rate limiting check
    current_time = time.time()
    if current_time - last_request_time < MIN_INTERVAL:
        return jsonify({"error": "Too many requests. Please wait."}), 429
    
    last_request_time = current_time
    
    data = request.json
    user_message = data.get("message")
    
    # Using client.chats to maintain context
    # In a real app, you'd use a unique session ID to manage different users' chats
    chat_session = client.chats.create(model="gemini-2.5-flash")
    response = chat_session.send_message(user_message)
    
    return jsonify({"response": response.text})

if __name__ == '__main__':
    app.run(port=5000)
