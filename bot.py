from dotenv import dotenv_values
from telebot.async_telebot import AsyncTeleBot 

from api.rcon import RconServer 

config = dotenv_values(".env")

class Bot(AsyncTeleBot):
    def __init__(self):
        super().__init__(config.get("TELEGRAM_API_TOKEN"))

        host = config.get("RCON_HOST")
        port = config.get("RCON_PORT")
        password = config.get("RCON_PASSWORD")

        self._rconServer = RconServer(host, port, password)

    async def sendWelcom(self, message):
        await self.send_message(message.chat.id, "Привет! 👋😃")

    async def serverReload(self, message):
        self._rconServer.serverReload()
        await self.send_message(message.chat.id, f"🟢 Сервер успешно перезагружен")
