from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route to check if server is running
@app.route("/", methods=["GET"])
def home():
    return "Alexa skill backend is running!", 200

# Alexa request handler (Must accept POST)
@app.route("/alexa", methods=["POST"])
def alexa_skill():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data received"}), 400

        # Extract the intent name
        intent = data.get("request", {}).get("intent", {}).get("name", "")

        # Log the incoming request for debugging
        print("Received Alexa request:", data)

        if intent:
            response_text = f"Received intent: {intent}"
        else:
            response_text = "I didn't understand that command."

        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {"type": "PlainText", "text": response_text},
                "shouldEndSession": True
            }
        })
    
    except Exception as e:
        print("Error processing request:", str(e))
        return jsonify({"error": str(e)}), 500

# Ensure the app runs on port 8080 (not 10000)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
