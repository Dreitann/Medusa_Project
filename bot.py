import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.fsm.storage.memory import MemoryStorage
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # из .env файла

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    user_id = message.from_user.id
    room = f"room_{user_id}_{random.randint(1000, 9999)}"
    web_app_url = f"https://dreitann.github.io/Medusa_Project/index.html?room={room}"

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎥 Присоединиться к звонку", web_app=WebAppInfo(url=web_app_url))]
    ])

    await message.answer("👋 Нажми кнопку ниже, чтобы начать видеозвонок:", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
