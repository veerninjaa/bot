from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os

# === Configuration ===
TOKEN = "7742866090:AAGzLvBk8hnfSllLEnPcobBAUkhaEkOM2j8"  # Replace this with @veerninja_bot token
WEBHOOK_URL = f"https://veerninja.onrender.com/{TOKEN}"  # Replace with your Render domain

# === Flask App ===
app = Flask(__name__)

# === Telegram Bot Setup ===
bot = Bot(token=TOKEN)
dispatcher = Dispatcher(bot, None, use_context=True)

# === Command Handlers ===
def start(update, context):
    update.message.reply_text("Welcome to VeerNinja! 🥷 This bot simulates phishing for learning purposes.")

def help_command(update, context):
    update.message.reply_text("Send a suspicious message to simulate a phishing attack!")

def echo(update, context):
    update.message.reply_text("You said: " + update.message.text)

# Register handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help_command))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# === Webhook Route ===
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# === Root Route (Optional) ===
@app.route("/", methods=["GET"])
def index():
    return "VeerNinja bot is running!"

# === Set Webhook on First Request ===
@app.before_request
def set_webhook_once():
    if not hasattr(app, 'webhook_set'):
        bot.set_webhook(WEBHOOK_URL)
        app.webhook_set = True

# === Entry Point ===
if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)))
