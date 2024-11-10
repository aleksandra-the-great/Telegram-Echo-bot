# from flask import Flask, request, jsonify
# import telebot
# import os

# app = Flask(__name__)

# # Получаем токен из переменной окружения
# TOKEN = os.getenv("TOKEN")
# WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # URL для вебхука

# # Проверка на случай, если токен или URL отсутствуют
# if TOKEN is None:
#     raise ValueError("TOKEN is not set. Please set the TELEGRAM_BOT_TOKEN environment variable.")
# if WEBHOOK_URL is None:
#     raise ValueError("WEBHOOK_URL is not set. Please set the WEBHOOK_URL environment variable.")

# bot = telebot.TeleBot(TOKEN)

# # Устанавливаем вебхук
# @app.route('/setwebhook', methods=['GET'])
# def set_webhook():
#     full_webhook_url = WEBHOOK_URL + '/webhook'
#     print("Setting webhook to:", full_webhook_url)  # Логирование для проверки
#     webhook = bot.set_webhook(url=full_webhook_url)
#     if webhook:
#         return jsonify({"status": "Webhook set successfully"}), 200
#     else:
#         return jsonify({"status": "Failed to set webhook"}), 400

# # Обрабатываем сообщения от Telegram через вебхук
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.get_json()
#     message = data.get("message", "")
#     user_id = data.get("message", {}).get("from", {}).get("id", "")

#     # Проверяем, что message и user_id определены, чтобы избежать ошибки
#     if message and user_id:
#         bot.send_message(user_id, message["text"])  # Отправляем ответ пользователю
#     return jsonify({"status": "ok"})

# if __name__ == "__main__":
#     # Запуск приложения Flask
#     app.run(host="0.0.0.0", port=5000)


from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Отправляем HTML страницу с встроенным JS кодом
    return render_template('accounter.html')

if __name__ == "__main__":
    app.run()
