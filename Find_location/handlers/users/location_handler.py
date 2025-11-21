from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default.loc_button import keyboard
from keyboards.default.loc_button import keyboard
from utils.misc.get_distance import choose_shortest
from utils.misc.get_distance import choose_short_hotel
from loader import dp
from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from utils.misc.get_distance import choose_short_hospital
from utils.misc.get_distance import choose_short_shop
@dp.callback_query_handler(text="mylocation")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Lokatsiya yuboring;", reply_markup=keyboard)






user_choice = {}


@dp.callback_query_handler(text="myhotel")
async def hotel_choice(call: CallbackQuery):
    user_choice[call.from_user.id] = "hotel"
    await call.message.answer("Lokatsiyani yuboring 📍", reply_markup=keyboard)
    await call.answer()

# Callback handler: masjid tanlandi
@dp.callback_query_handler(text="mymasjid")
async def masjid_choice(call: CallbackQuery):
    user_choice[call.from_user.id] = "masjid"
    await call.message.answer("Lokatsiyani yuboring 📍", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="myhospital")
async def masjid_choice(call: CallbackQuery):
    user_choice[call.from_user.id] = "myhospital"
    await call.message.answer("Lokatsiyani yuboring 📍", reply_markup=keyboard)
    await call.answer()


@dp.callback_query_handler(text="myshop")
async def masjid_choice(call: CallbackQuery):
    user_choice[call.from_user.id] = "myshop"
    await call.message.answer("Lokatsiyani yuboring 📍", reply_markup=keyboard)
    await call.answer()


# Location handler
@dp.message_handler(content_types=['location'])
async def get_contact(message: Message):
    user_id = message.from_user.id
    choice = user_choice.get(user_id)

    if choice == "hotel":
        closest_shops = choose_short_hotel(message.location)
    elif choice == "masjid":
        closest_shops = choose_shortest(message.location)
    elif choice == "myhospital":
        closest_shops = choose_short_hospital(message.location)
    elif choice == "myshop":
        closest_shops = choose_short_shop(message.location)
    else:
        await message.answer("Avval mehmonxona yoki masjidni tanlang.")
        return

    latitude = message.location.latitude
    longitude = message.location.longitude

    text = "\n\n".join([
        f"<a href='{url}'>{shop_name}</a>\n Masofa: {distance:.1f} km."
        for shop_name, distance, url, shop_location in closest_shops
    ])

    await message.answer(
        f"Sizning joylashuv!📍 \n"
        f"Kenglik = {latitude}\n"
        f"Uzunlik = {longitude}\n\n"
        f"{text}",
        disable_web_page_preview=True,
        reply_markup=keyboard
    )

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(
            latitude=shop_location["lat"],
            longitude=shop_location["lon"]
        )

    # Agar kerak bo'lsa, tanlovni o'chirib qo'yish
    user_choice.pop(user_id, None)
