from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
import asyncio

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🦷 Shoxjaxon Lab Botga xush kelibsiz!\n\n"
        "Bu bot orqali doktorlar, ishlar va to'lovlarni boshqarishingiz mumkin."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
TOKEN =  8697156844: AAExau5HVpzJbYp8RRS_2
RbFj3KZKfI3p6I 
  
