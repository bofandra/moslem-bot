import logging
from gradio_client import Client
import asyncio

from aiogram import Bot, Dispatcher, types

API_TOKEN = '6546697966:AAH3K0GvgvnMy6AWn43xYKi_3fuRyzEhqAw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

client = Client("Bofandra/moslem-bot")

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Please ask anything about Islam..")



@dp.message_handler()
async def echo(message: types.Message):
    print("echo")
    print(message)
    job = client.submit(
		message=message,
		max_tokens=2048,
		temperature=0.7,
		top_p=0.95,
		api_name="/chat"
    )
    await message.answer(job.result())

async def main():
    print('Bot started')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())