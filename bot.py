from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import config



logging.basicConfig(format='[%(asctime)s] [%(levelname)s]: %(message)s',
                    datefmt="%Y/%m/%d, %H:%M:%S",
                    level=logging.INFO,
                    filename = 'bot.log'
                    )

def main():
    bot = Updater(config.API_TOKEN)
    logging.info("Bot is starting...")

    dp = bot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("info", user_info))
    dp.add_handler(MessageHandler(Filters.text, user_dialogue))

    bot.start_polling()
    logging.info("Bot started successfully.")
    bot.idle()

def greet_user(bot, update):
    reply_text = "S-sup!"
    update.message.reply_text(reply_text)
    logging.info("(Chat ID: %s) %s issued command: /start", update.message.chat.id, update.message.chat.username)
    logging.info("(Chat ID: %s) [Bot] %s", update.message.chat.id, reply_text)

def user_info(bot, update):
    user_info = "{}'s account info:\nID: {}\nUsername: {}\nFirst name: {}".format(update.message.chat.first_name, update.message.chat.id, update.message.chat.username, update.message.chat.first_name)
    update.message.reply_text(user_info)
    logging.info("(Chat ID: %s) %s issued command: /info", update.message.chat.id, update.message.chat.username)
    logging.info("(Chat ID: %s) [Bot] %s", update.message.chat.id, user_info)

def user_dialogue(bot, update):
    user_text = update.message.text
    update.message.reply_text(user_text)
    logging.info("(Chat ID: %s) <%s> %s", update.message.chat.id, update.message.chat.username, user_text)
    logging.info("(Chat ID: %s) [Bot] %s", update.message.chat.id, user_text)

main()
