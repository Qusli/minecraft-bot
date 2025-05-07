from bot import Bot

bot = Bot()

@bot.message_handler("start")
def sendWelcom(message):
    bot.sendWelcom(message)

@bot.message_handler("restart")
def serverRestart(message):
    bot.serverRestart(message)

bot.infinity_polling()