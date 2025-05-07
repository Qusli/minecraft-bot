import asyncio

from bot import Bot

bot = Bot()

@bot.message_handler("start")
async def sendWelcom(message):
    await bot.sendWelcom(message)

@bot.message_handler("restart")
async def serverRestart(message):
    await bot.serverRestart(message)

asyncio.run(bot.polling())