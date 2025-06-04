from flask import Flask, request
import requests
import os

app = Flask(__name__)

TG_API_URL = f"https://api.telegram.org/bot{os.environ.get('BOT_TOKEN')}/sendMessage"
CHAT_ID = os.environ.get("CHAT_ID")

@app.route('/send-signal', methods=['POST'])
def send_signal():
    try:
        raw_text = request.get_data(as_text=True)
        message = raw_text if raw_text.strip() else "⚠️ 沒有收到內容"
    except Exception as e:
        message = f"❌ 錯誤：{str(e)}"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(TG_API_URL, json=payload)

    return "ok", 200

