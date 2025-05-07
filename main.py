from bot import Bot

bot = Bot()

@bot.message_handler("start")
def sendWelcom(message):
    bot.sendWelcom(message)

@bot.message_handler("reload")
def serverReload(message):
    bot.serverReload(message)

bot.infinity_polling()