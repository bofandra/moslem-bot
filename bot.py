import logging
from gradio_client import Client

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

API_TOKEN = '6546697966:AAH3K0GvgvnMy6AWn43xYKi_3fuRyzEhqAw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

client = Client("Bofandra/moslem-bot")

@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` command
    """
    await message.reply("Please ask anything about Islam..")



@dp.message()
async def echo(message: types.Message):
    print("echo")
    print(message.text)
    """result = client.predict(
		message=message.text,
		max_tokens=2048,
		temperature=0.7,
		top_p=0.95,
		api_name="/chat"
    )"""
    await message.answer(message.text)

if __name__ == "__main__":
    dp.start_polling(bot)