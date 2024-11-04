// Инициализация Telegram WebApp API
Telegram.WebApp.ready();

function sendData() {
    const message = document.getElementById("messageInput").value;
    if (message) {
        // Отправляем сообщение боту
        Telegram.WebApp.sendData(message);
    }
}

// Обрабатываем сообщение от бота
window.Telegram.WebApp.onEvent("message", function(data) {
    document.getElementById("responseOutput").innerText = `Echo: ${data}`;
});
