from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

keyboard=ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[

        [
            KeyboardButton(text="🗾 Locatsiya",request_location=True),
            KeyboardButton(text="☎️ Telfon raqam",request_contact=True)
        ],
        [
            KeyboardButton(text="🤖 Bot Haqida")
        ]
    ]
)


























