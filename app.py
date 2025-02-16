{\rtf1\ansi\ansicpg1252\cocoartf2818
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from flask import Flask, request, jsonify\
\
app = Flask(__name__)\
\
@app.route('/alexa', methods=['POST'])\
def alexa_skill():\
    data = request.json\
    intent = data.get('request', \{\}).get('intent', \{\}).get('name', '')\
\
    if intent == "SetTemperatureIntent":\
        room = data['request']['intent']['slots']['room']['value']\
        temp = data['request']['intent']['slots']['temperature']['value']\
        return jsonify(\{\
            "version": "1.0",\
            "response": \{\
                "outputSpeech": \{"type": "PlainText", "text": f"Setting \{room\} to \{temp\} degrees."\},\
                "shouldEndSession": True\
            \}\
        \})\
\
    return jsonify(\{"version": "1.0", "response": \{"shouldEndSession": True\}\})\
\
if __name__ == "__main__":\
    app.run(host="0.0.0.0", port=8080)\
}