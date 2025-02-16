from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/alexa', methods=['POST'])
def alexa_skill():
    data = request.json
    intent = data.get('request', {}).get('intent', {}).get('name', '')

    if intent == "SetTemperatureIntent":
        room = data['request']['intent']['slots']['room']['value']
        temp = data['request']['intent']['slots']['temperature']['value']
        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {"type": "PlainText", "text": f"Setting {room} to {temp} degrees."},
                "shouldEndSession": True
            }
        })

    return jsonify({"version": "1.0", "response": {"shouldEndSession": True}})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)