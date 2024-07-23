import logging
logging.basicConfig(level=logging.INFO)
from gradio_client import Client
from telegram.ext import Updater, CommandHandler, MessageHandler

TOKEN = "later"

def start(update, context):
    update.message.reply_text("Welcome to the moslem bot! I can help you with your questions. send /ask ")

def ask(update, context):
    client = Client("Bofandra/moslem-bot")
    query = update.message.text
    result = client.predict(
		message=query,
		max_tokens=2048,
		temperature=0.7,
		top_p=0.95,
		api_name="/chat"
    )
    update.message.reply_text(result)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ask", ask))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()