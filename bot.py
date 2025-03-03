from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Reemplaza con tu token de bot de Telegram
TOKEN = "8068879567:AAFFh_CiTpHnJ2ahU_A5E34601W-KcEgToQ"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("¡Hola! Soy un bot de Telegram. Usa /help para más opciones.")

def main():
    # Crea el bot y lo conecta con Telegram
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Comandos del bot
    dp.add_handler(CommandHandler("start", start))

    # Inicia el bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
