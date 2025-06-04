from flask import Flask, request
import requests
import os

app = Flask(__name__)

# 環境變數
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
TG_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

@app.route('/send-signal', methods=['POST'])
def send_signal():
    try:
        data = request.get_json()

        signal_type = data.get("type", "訊號")
        time = data.get("time", "N/A")
        entry = data.get("entry", "N/A")
        tp1 = data.get("tp1", "N/A")
        tp2 = data.get("tp2", "N/A")
        tp3 = data.get("tp3", "N/A")
        sl = data.get("sl", "N/A")
        symbol = data.get("symbol", "XAUUSD")

        message = f"""📢 {symbol} 快訊  
{"📈 BUY Signal 出現！" if signal_type == "BUY" else "📉 Sell Signal 出現！"}

🕒 時間：{time}
💵 進場價：{entry}

🎯 TP1：{tp1}
🎯 TP2：{tp2}
🎯 TP3：{tp3}
🛡 Stop Loss：{sl}
"""

    except Exception as e:
        # 如果不是 JSON 格式，就原樣轉發原始文字
        raw_text = request.get_data(as_text=True)
        message = raw_text if raw_text else "❌ 無資料"

    # 發送訊息到 Telegram
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(TG_API_URL, json=payload)
    return "ok", 200

if __name__ == '__main__':
    app.run()
