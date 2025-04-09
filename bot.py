from telegram.ext import Updater, CommandHandler
import logging

# Replace this with your bot token
TOKEN = "7742866090:AAGzLvBk8hnfSllLEnPcobBAUkhaEkOM2j8"

logging.basicConfig(level=logging.INFO)

def start(update, context):
    update.message.reply_text(
        "🎯 Welcome to the Phishing Simulator!\n\nClick below to simulate a login page:\n"
        "https://veerninja-bot.onrender.com"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
