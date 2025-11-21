from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

keys = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏩Eng yaqin mehmonxona",callback_data="myhotel")
        ],
        [
            InlineKeyboardButton(text="🛍️Eng yaqin dokon",callback_data="myshop")
        ],
        [
            InlineKeyboardButton(text="🏥Eng yaqin shifoxona",callback_data="myhospital")
        ],
        [
            InlineKeyboardButton(text="🕌Eng yaqin masjid topish", callback_data="mymasjid")
        ]
])
