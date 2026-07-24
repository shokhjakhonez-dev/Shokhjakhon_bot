from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🦷 Yangi ish"),
            KeyboardButton(text="📋 Ishlar")
        ],
        [
            KeyboardButton(text="👨‍⚕️ Doktorlar"),
            KeyboardButton(text="🎓 Shogirtlar")
        ],
        [
            KeyboardButton(text="💰 To'lovlar"),
            KeyboardButton(text="📊 Hisobot")
        ],
        [
            KeyboardButton(text="⚙️ Sozlamalar")
        ]
    ],
    resize_keyboard=True
)
