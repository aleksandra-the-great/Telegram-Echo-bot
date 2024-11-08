from flask import Flask, request, jsonify
import telebot
import os

app = Flask(__name__)

# Получаем токен из переменной окружения
TOKEN = os.getenv("TOKEN")
print(TOKEN)
# Проверка на случай, если токен отсутствует
if TOKEN is None:
    raise ValueError("TOKEN is not set. Please set the TELEGRAM_BOT_TOKEN environment variable.")

bot = telebot.TeleBot(TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data.get("message", "")
    user_id = data.get("user_id", "")
    # Проверяем, что user_id определен, чтобы избежать ошибки
    if user_id:
        bot.send_message(user_id, message)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)
