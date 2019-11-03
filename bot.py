from telegram.ext import Updater, CommandHandler
import logging



logging.basicConfig(format='[%(asctime)s] [%(levelname)s]: %(message)s',
                    datefmt="%Y/%m/%d, %H:%M:%S",
                    level=logging.INFO,
                    filename = 'bot.log'
                    )

def main():
    bot = Updater('1027387265:AAGoKkRBl04IFFneRDRKcsh7H7rZIAGLOns')
    logging.info("Bot is starting...")

    dp = bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    bot.start_polling()
    logging.info("Bot started successfully.")
    bot.idle()

def greet_user(bot, update):
    reply_text = "Привет! Чем я могу быть полезен?"
    update.message.reply_text(reply_text)
    logging.info(reply_text)

main()