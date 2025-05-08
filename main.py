import asyncio

from bot import Bot

bot = Bot()

@bot.message_handler("start")
async def sendWelcom(message):
    await bot.sendWelcom(message)

@bot.message_handler("reload")
async def serverReload(message):
    await bot.serverReload(message)

@bot.message_handler("teleport")
async def teleport(message):
    args = message.text.split(' ')

    targets = args[0]
    location = args[1]

    await bot.teleport(message, targets, location)

asyncio.run(bot.polling())