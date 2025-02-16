from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined temperature adjustments
TEMPERATURE_PRESETS = {
    "hot": 76,  # Set temperature to 76°F when it's hot
    "cold": 77  # Set temperature to 77°F when it's cold
}

@app.route('/alexa', methods=['POST'])
def alexa_skill():
    data = request.json
    intent = data.get('request', {}).get('intent', {}).get('name', '')

    # Handle "It's hot in here"
    if intent == "AdjustTemperatureIntent":
        if "hot" in data['request']['intent']['slots']:
            new_temp = TEMPERATURE_PRESETS["hot"]
            response_text = f"Lowering the temperature to {new_temp} degrees."
        elif "cold" in data['request']['intent']['slots']:
            new_temp = TEMPERATURE_PRESETS["cold"]
            response_text = f"Raising the temperature to {new_temp} degrees."
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
