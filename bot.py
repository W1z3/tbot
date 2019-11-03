from telegram.ext import Updater



def main():
    bot = Updater('1027387265:AAGoKkRBl04IFFneRDRKcsh7H7rZIAGLOns')
    bot.start_polling()
    bot.idle()

main()