from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = '7972145542:AAGrGpfx8_pdCyJSAIUH-W3XWViGAoUpBzI'
CHAT_ID = '-1002518915115'

@app.route('/send-signal', methods=['POST'])
def send_signal():
    data = request.get_json()

    signal_type = data.get('type', '訊號')
    emoji = '📈' if signal_type.upper() == 'BUY' else '📉'

    message = f"""
📢 *XAUUSD 快訊*

{emoji} *{signal_type} Signal 出現！*

🪙 商品：*{data.get('symbol', 'XAUUSD')}*  
🕰️ 時間：*{data.get('time', '未提供')}*  
💵 進場價：*{data.get('entry', '未提供')}*  

🎯 TP1：*{data.get('tp1', '')}*  
🎯 TP2：*{data.get('tp2', '')}*  
🎯 TP3：*{data.get('tp3', '')}*  
🛡️ Stop Loss：*{data.get('sl', '')}*
"""

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'parse_mode': 'Markdown'
    }

    response = requests.post(telegram_url, json=payload)
    return {'ok': True, 'telegram_response': response.json()}