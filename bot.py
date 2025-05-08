from dotenv import dotenv_values
from telebot.async_telebot import AsyncTeleBot 

from api.rcon import RconServer 
from decorator.check_permission import CheckPermissionByWhitelist

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

    @CheckPermissionByWhitelist
    async def serverReload(self, message):
        self._rconServer.serverReload()
        await self.send_message(message.chat.id, f"🟢 Сервер успешно перезагружен")

    @CheckPermissionByWhitelist
    async def teleport(self, message, targets: str, location: str | None):
        if targets is None:
            await self.send_message(message.chat.id, f"🔴 Первый параметр обязательный!")
            return
        
        self._rconServer.teleport(targets, location)

        if location is None:
            await self.send_message(message.chat.id, f"🟢 Пользователь {targets} успешно телепортирован")
        else:
            await self.send_message(message.chat.id, f"🟢 Пользователь {targets} успешно телепортирован к {location}")