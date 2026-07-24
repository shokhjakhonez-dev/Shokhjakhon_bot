from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(Command("doctors"))
async def doctors(message: Message):
    await message.answer(
        "👨‍⚕️ Doktorlar bo'limi\n\n"
        "Bu yerda keyinchalik doktor qo'shish, o'chirish va ro'yxatini ko'rish imkoniyati bo'ladi."
    )
