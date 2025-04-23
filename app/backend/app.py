# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)  

quotes = [
    "Believe you can and you're halfway there.",
    "Do not watch the clock. Do what it does. Keep going.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "It does not matter how slowly you go as long as you do not stop.",
    "Everything you've ever wanted is on the other side of fear.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Believe in yourself, take on your challenges, dig deep within yourself to conquer fears.",
    "Your time is limited, don't waste it living someone else's life.",
    "The best way to predict the future is to create it."
]

@app.route('/api/quote', methods=['GET'])
def get_quote():
    quote = random.choice(quotes)
    return jsonify({"quote": quote})

if __name__ == '__main__':
    app.run(debug=True)