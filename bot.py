from telegram.ext import Updater, CommandHandler
from threading import Thread
import server
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("✅ Veerninja_bot is running!\n⚠️ Educational use only!")

def help_command(update, context):
    update.message.reply_text("Commands:\n/start - Start the bot\n/help - Show this help")

def run_bot():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    Thread(target=server.app.run, kwargs={"host": "0.0.0.0", "port": 10000}).start()
    run_bot()
