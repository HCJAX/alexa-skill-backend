from flask import Flask, request, jsonify

app = Flask(__name__)

# Health check route to verify the service is live
@app.route("/", methods=["GET"])
def home():
    return "Alexa skill backend is running!", 200

# Alexa requests handler
@app.route("/alexa", methods=["POST"])
def alexa_skill():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data received"}), 400

        intent = data.get("request", {}).get("intent", {}).get("name", "")

        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {"type": "PlainText", "text": f"Received intent: {intent}"},
                "shouldEndSession": True
            }
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

