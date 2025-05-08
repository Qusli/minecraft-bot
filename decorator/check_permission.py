from dotenv import dotenv_values

config = dotenv_values(".env")

whitelist = config.get("WHITE_LIST") # "1000000, 1000001" - this user telegram ids

if whitelist is not None:
    whitelist = whitelist.split(',')

if not whitelist:
    whitelist = list()

def CheckPermissionByWhitelist(func):
    async def wrapper(self, *args, **kwargs):
        message = args[0]

        telegramUserId = str(message.from_user.id)

        if telegramUserId not in whitelist:
            await self.send_message(message.chat.id, "🔴 У Вас нет прав, на использование данных команд.")
            return

        return await func(self, *args, **kwargs)
    return wrapper