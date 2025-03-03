import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Obtener el TOKEN desde Railway
TOKEN = os.getenv("TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("¡Hola! Soy un bot de Telegram funcionando en Railway.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
