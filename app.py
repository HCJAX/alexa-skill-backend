from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined temperature settings
TEMPERATURE_PRESETS = {
    "hot": 76,  # Set temperature to 76°F when it's hot
    "cold": 77  # Set temperature to 77°F when it's cold
}

@app.route('/alexa', methods=['POST'])
def alexa_skill():
    data = request.json
    intent = data.get('request', {}).get('intent', {}).get('name', '')

    if intent == "AdjustTemperatureIntent":
        slots = data.get('request', {}).get('intent', {}).get('slots', {})

        # Ensure Alexa has provided a room (since it's required)
        if "room" in slots and "value" in slots["room"]:
            room = slots["room"]["value"]
        else:
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {"type": "PlainText", "text": "I didn't get the room name. Can you say it again?"},
                    "shouldEndSession": False
                }
            })

        # Check if the request is for hot or cold adjustment
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
