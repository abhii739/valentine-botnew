
from flask import Flask, render_template, request, jsonify
import random, string

app = Flask(__name__)

responses = {
    "yes": ["Yayyy! 💖 You said YES!", "Happy Valentine’s Day ❤️", "Let’s celebrate together! 🎉"],
    "no": ["Please think again 🥺","Are you Sure 🥺","\U0001F494"],
    "default": ["Type yes or no 😄"]
}

keywords = {"yes":["yes"],"no":["no"]}

def preprocess(t):
    return t.lower().translate(str.maketrans('','',string.punctuation)).split()

def reply(msg):
    tokens=preprocess(msg)
    for k,w in keywords.items():
        if any(x in tokens for x in w):
            return random.choice(responses[k])
    return random.choice(responses["default"])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    return jsonify({"reply": reply(request.json["message"])})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
