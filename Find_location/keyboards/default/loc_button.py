from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                               keyboard=[
                                   [
                                       KeyboardButton(text="/manzil"),
                                       KeyboardButton(text="Joylashuvimni yuborish 📍", request_location=True)

                                   ]
                               ])