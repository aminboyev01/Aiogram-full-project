from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart,Command
from keyboards.default.loc_button import keyboard
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Assalomu aleykum, {message.from_user.full_name}\nEng yaqin xizmat ko‘rsatish\ntopish uchun /manzil yuboring!",reply_markup=keyboard)

# @dp.message_handler(Command("hotel"))
# async def

