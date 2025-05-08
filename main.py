import asyncio

from bot import Bot

bot = Bot()

@bot.message_handler("start")
async def sendWelcom(message):
    await bot.sendWelcom(message)

@bot.message_handler("tps")
async def getTPS(message):
    await bot.getTPS(message)

@bot.message_handler("list")
async def getPlayers(message):
    await bot.getPlayers(message)

@bot.message_handler("op")
async def op(message):
    args = message.text.split(' ')

    target = None

    if len(args) > 1:
        target = args[1]

    await bot.op(message, target)

@bot.message_handler("deop")
async def deop(message):
    args = message.text.split(' ')

    target = None

    if len(args) > 1:
        target = args[1]

    await bot.deop(message, target)

@bot.message_handler("reload")
async def serverReload(message):
    await bot.serverReload(message)

@bot.message_handler("teleport")
async def teleport(message):
    args = message.text.split(' ')

    targets = None
    location = None

    if len(args) > 1:
        targets = args[1]

    if len(args) > 2:
        location = args[2]

    await bot.teleport(message, targets, location)

@bot.message_handler("kick")
async def kick(message):
    args = message.text.split(' ')

    target = None
    reason = None

    if len(args) > 1:
        target = args[1]

    if len(args) > 2:
        reason = args[2]

    await bot.kick(message, target, reason)

@bot.message_handler("ban")
async def ban(message):
    args = message.text.split(' ')

    target = None
    reason = None

    if len(args) > 1:
        target = args[1]

    if len(args) > 2:
        reason = args[2]

    await bot.ban(message, target, reason)

@bot.message_handler("unban")
async def unban(message):
    args = message.text.split(' ')

    target = None

    if len(args) > 1:
        target = args[1]

    await bot.unban(message, target)

asyncio.run(bot.polling())