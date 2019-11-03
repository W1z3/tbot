from telegram.ext import Updater, CommandHandler



def main():
    bot = Updater('1027387265:AAGoKkRBl04IFFneRDRKcsh7H7rZIAGLOns')

    dp = bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    bot.start_polling()
    bot.idle()

def greet_user(bot, update):
    reply_text = "Добро пожаловать! Чем я могу быть полезен?"
    print(reply_text)
    update.message.reply_text(reply_text) 

main()