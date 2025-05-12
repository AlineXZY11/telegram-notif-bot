#!/usr/bin/env python3
from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv("7631244427:AAE5VXJqR_nwNek3ABaIZgM9WNDMAFichxw")
CHAT_ID = os.getenv("78999815")
SECRET_KEY = os.getenv("112552#Root")  # Untuk autentikasi

@app.route('/notify', methods=['POST'])
def notify():
    if request.headers.get('X-Secret-Key') != SECRET_KEY:
        return "Unauthorized", 401
    
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
