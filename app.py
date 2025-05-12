#!/usr/bin/env python3
from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("7598964683:AAE4BFqHIXcFRhkVNzbF1d42LAmNX6jfvGY")  # Ambil dari Environment Variables
CHAT_ID = os.getenv("789995815")

@app.route('/notify', methods=['POST'])
def notify():
    message = request.json.get("message")
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)
    return "Notifikasi terkirim!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
