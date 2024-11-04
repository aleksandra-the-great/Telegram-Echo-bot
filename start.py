from flask import Flask, request, jsonify
import telebot



app = Flask(__name__)
TOKEN = '7124362675:AAGJhFXcJUpiLQKU9uZTYCkvRRumWkJ7BTM'
bot = telebot.TeleBot(TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", "")
    # Отправляем сообщение обратно пользователю
    bot.send_message(data["user_id"], message)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)
