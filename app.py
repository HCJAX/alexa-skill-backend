from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined temperature settings
TEMPERATURE_PRESETS = {
    "hot": 76,  
    "cold": 77  
}

@app.route('/alexa', methods=['POST'])
def alexa_skill():
    try:
        # Ensure the request is in JSON format
        if not request.is_json:
            return jsonify({"error": "Request must be in JSON format"}), 400
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON request"}), 400

        intent = data.get('request', {}).get('intent', {}).get('name', '')

        if intent == "AdjustTemperatureIntent":
            slots = data.get('request', {}).get('intent', {}).get('slots', {})
            room = slots.get("room", {}).get("value", "living room")  

            if "hot" in slots:
                new_temp = TEMPERATURE_PRESETS["hot"]
                response_text = f"Lowering the temperature in the {room} to {new_temp} degrees."
            elif "cold" in slots:
                new_temp = TEMPERATURE_PRESETS["cold"]
                response_text = f"Raising the temperature in the {room} to {new_temp} degrees."
            else:
                response_text = "I didn't catch that. Are you feeling hot or cold?"

            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {"type": "PlainText", "text": response_text},
                    "shouldEndSession": True
                }
            })

        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {"type": "PlainText", "text": "I didn't understand that."},
                "shouldEndSession": True
            }
        })

    except Exception as e:
        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {"type": "PlainText", "text": "There was an error processing your request."},
                "shouldEndSession": True
            }
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)