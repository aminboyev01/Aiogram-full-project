from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_keyboard = [[
    InlineKeyboardButton(text="/start", callback_data='start'),
    InlineKeyboardButton(text="/help", callback_data='help')
]



]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
