from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route for testing if the server is running
@app.route("/", methods=["GET"])
def home():
    return "Alexa skill backend is running!", 200

# Alexa request handler
@app.route("/alexa", methods=["POST"])
def alexa_skill():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data received"}), 400

        # Log the full request for debugging
        print("Received Alexa request:", data)

        request_type = data.get("request", {}).get("type", "")
        intent = data.get("request", {}).get("intent", {}).get("name", "")

        # ✅ Handle LaunchRequest (Opening the skill)
        if request_type == "LaunchRequest":
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "Welcome to Chatbot Control. How can I help?"
                    },
                    "shouldEndSession": False
                }
            })

        # ✅ Handle IntentRequests (Commands like "It's hot in here")
        elif request_type == "IntentRequest":
            response_text = f"Received intent: {intent}" if intent else "I didn't understand that command."
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {"type": "PlainText", "text": response_text},
                    "shouldEndSession": True
                }
            })

        # ✅ Handle unexpected requests
        else:
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {"type": "PlainText", "text": "Sorry, I didn't understand that request."},
                    "shouldEndSession": True
                }
            })

    except Exception as e:
        print("Error processing request:", str(e))
        return jsonify({"error": str(e)}), 500

# Ensure Flask runs on port 8080
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

