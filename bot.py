import re

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

    async def getTPS(self, message):
        tps = self._rconServer.getTPS()

        tps = re.sub(r"§.", "", tps)

        await self.send_message(message.chat.id, tps)

    async def getPlayers(self, message):
        list = self._rconServer.getPlayers()
        
        await self.send_message(message.chat.id, list)

    @CheckPermissionByWhitelist
    async def serverReload(self, message):
        self._rconServer.serverReload()
        await self.send_message(message.chat.id, f"🟢 Сервер успешно перезагружен")

    @CheckPermissionByWhitelist
    async def teleport(self, message, targets: str, location: str):
        if targets is None:
            await self.send_message(message.chat.id, f"🔴 Нужно указать пользователя, которого нужно телепортировать!")
            return
        
        if location is None:
            await self.send_message(message.chat.id, f"🔴 Нужно указать пользователя, к которому нужно телепортировать")
            return
        
        self._rconServer.teleport(targets, location)

        await self.send_message(message.chat.id, f"🟢 Пользователь {targets} успешно телепортирован к {location}")

    @CheckPermissionByWhitelist
    async def kick(self, message, target: str, reasone: str | None):
        if target is None:
            await self.send_message(message.chat.id, f"🔴 Нужно обязательно указать ник пользователя!")
            return
        
        self._rconServer.kick(target, reasone)

        await self.send_message(message.chat.id, f"🟢 Пользователь {target} успешно кикнут с сервера")
    
    @CheckPermissionByWhitelist
    async def ban(self, message, target: str, reasone: str | None):
        if target is None:
            await self.send_message(message.chat.id, f"🔴 Нужно обязательно указать ник пользователя!")
            return
        
        self._rconServer.ban(target, reasone)

        await self.send_message(message.chat.id, f"🟢 Пользователь {target} успешно забанен на сервере")

    @CheckPermissionByWhitelist
    async def unban(self, message, target: str):
        if target is None:
            await self.send_message(message.chat.id, f"🔴 Нужно обязательно указать ник пользователя!")
            return
        
        self._rconServer.unban(target)

        await self.send_message(message.chat.id, f"🟢 Пользователь {target} успешно разбанен на сервере")