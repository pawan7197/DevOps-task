from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success is not final; failure is not fatal.",
    "Dream it. Wish it. Do it."
]

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

