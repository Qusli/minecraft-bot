import telebot

from dotenv import dotenv_values
import telebot.async_telebot

from api.rcon import RconServer 

config = dotenv_values(".env")

class Bot(telebot.async_telebot.AsyncTeleBot):
    def __init__(self):
        super().__init__(config.get("TELEGRAM_API_TOKEN"))

        host = config.get("RCON_HOST")
        port = config.get("RCON_PORT")
        password = config.get("RCON_PASSWORD")

        self._rconServer = RconServer(host, port, password)

    async def sendWelcom(self, message):
        self.send_message(message.chat.id, "Привет! 👋😃")

    async def serverRestart(self, message):
        await self._rconServer.serverRestart()
        self.send_message(message.chat.id, f"🟢 Сервер успешно перезагружен")
