import telebot

from dotenv import dotenv_values

from api.rcon import RconServer 

config = dotenv_values(".env")

class Bot(telebot.TeleBot):
    def __init__(self):
        super().__init__(config.get("TELEGRAM_API_TOKEN"))

        host = config.get("RCON_HOST")
        port = config.get("RCON_PORT")
        password = config.get("RCON_PASSWORD")

        self._rconServer = RconServer(host, port, password)

    def sendWelcom(self, message):
        self.send_message(message.chat.id, "Привет! 👋😃")

    def serverRestart(self, message):
        self._rconServer.serverRestart()
        self.send_message(message.chat.id, f"🟢 Сервер успешно перезагружен")
