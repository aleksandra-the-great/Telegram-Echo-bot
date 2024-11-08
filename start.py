from flask import Flask, request, jsonify
import telebot
import os

app = Flask(__name__)

# Получаем токен из переменной окружения
TOKEN = os.getenv("TOKEN")

# Проверка на случай, если токен отсутствует
if TOKEN is None:
    raise ValueError("TOKEN is not set. Please set the TELEGRAM_BOT_TOKEN environment variable.")

bot = telebot.TeleBot(TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", "")
    user_id = data.get("user_id", None)
    
    if user_id:
        # Отправляем сообщение обратно пользователю
        bot.send_message(user_id, message)
    else:
        return jsonify({"status": "error", "message": "user_id is missing"}), 400
    
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)
