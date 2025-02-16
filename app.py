from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route to confirm the server is running
@app.route("/", methods=["GET"])
def home():
    return "Alexa skill backend is running!", 200

# Handle Alexa requests at /alexa
@app.route("/alexa", methods=["POST"])
def alexa_skill():
    data = request.json
    intent = data.get('request', {}).get('intent', {}).get('name', '')

    # Simple response to confirm Alexa requests are received
    return jsonify({
        "version": "1.0",
        "response": {
            "outputSpeech": {"type": "PlainText", "text": f"Received intent: {intent}"},
            "shouldEndSession": True
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)