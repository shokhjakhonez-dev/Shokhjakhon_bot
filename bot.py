import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN
from keyboards.menu import main_menu
from database.db import create_tables

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🦷 Shoxjaxon Lab tizimiga xush kelibsiz!\n\n"
        "Quyidagi menyudan kerakli bo'limni tanlang.",
        reply_markup=main_menu
    )


async def main():
    await create_tables()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
  
