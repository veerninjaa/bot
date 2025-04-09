from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

TOKEN = "7742866090:AAGzLvBk8hnfSllLEnPcobBAUkhaEkOM2j8"
bot = Bot(token=TOKEN)
app = Flask(__name__)
dispatcher = Dispatcher(bot, None, use_context=True)

# Example handler
def start(update, context):
    update.message.reply_text("Hello from webhook!")

dispatcher.add_handler(CommandHandler("start", start))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

@app.route("/", methods=["GET"])
def index():
    return "Bot is running"

# Set webhook (only once, not on every start)
@app.before_first_request
def set_webhook():
    bot.set_webhook(f"https://<https://veerninja.onrender.com>/{TOKEN}")
