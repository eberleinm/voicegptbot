from flask import Flask, request, render_template, jsonify
from bot_logic import get_gpt_response, speak_text, recognize_speech_from_mic

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_gpt_response(user_input)
    speak_text(response)
    return jsonify({"response": response})

@app.route("/speech", methods=["GET"])
def speech():
    recognized_text = recognize_speech_from_mic()
    return jsonify({"recognized": recognized_text})

if __name__ == "__main__":
    app.run(debug=True)
