import asyncio

from bot import Bot

bot = Bot()

@bot.message_handler("start")
async def sendWelcom(message):
    await bot.sendWelcom(message)

@bot.message_handler("reload")
async def serverReload(message):
    await bot.serverReload(message)

asyncio.run(bot.polling())