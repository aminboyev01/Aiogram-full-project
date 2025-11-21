from aiogram import Router, types,F
from aiogram.filters import CommandStart,Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.session.middlewares.request_logging import logger
from loader import db, bot
from data.config import ADMINS
from utils.extra_datas import make_title
from keyboards.reply.Button import keyboard
from keyboards.inline.buttons import are_you_sure_markup



router = Router()


@router.message(CommandStart())
async def do_start(message: types.Message):
    """
            MARKDOWN V2                     |     HTML
    link:   [Google](https://google.com/)   |     <a href='https://google.com/'>Google</a>
    bold:   *Qalin text*                    |     <b>Qalin text</b>
    italic: _Yotiq shriftdagi text_         |     <i>Yotiq shriftdagi text</i>



                    **************     Note     **************
    Markdownda _ * [ ] ( ) ~ ` > # + - = | { } . ! belgilari to'g'ridan to'g'ri ishlatilmaydi!!!
    Bu belgilarni ishlatish uchun oldidan \ qo'yish esdan chiqmasin. Masalan  \.  ko'rinishi . belgisini ishlatish uchun yozilgan.
    """

    telegram_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    user = None
    try:
        user = await db.add_user(telegram_id=telegram_id, full_name=full_name, username=username)
    except Exception as error:
        logger.info(error)
    if user:
        count = await db.count_users()
        msg = (f"[{make_title(user['full_name'])}](tg://user?id={user['telegram_id']}) bazaga qo'shildi\.\nBazada {count} ta foydalanuvchi bor\.")
    else:
        msg = f"[{make_title(full_name)}](tg://user?id={telegram_id}) bazaga oldin qo'shilgan"
    for admin in ADMINS:
        try:
            await bot.send_message(
                chat_id=admin,
                text=msg,
                parse_mode=ParseMode.MARKDOWN_V2
            )
        except Exception as error:
            logger.info(f"Data did not send to admin: {admin}. Error: {error}")
    await message.answer(f"Assalomu alaykum {make_title(full_name)}\!", parse_mode=ParseMode.MARKDOWN_V2,reply_markup=keyboard)




@router.message(F.location)
async def get_location(message:types.Message):
    latitude=message.location.latitude
    longitude=message.location.longitude
    await message.answer(f"🗺️Locatsiya qabul qilindi!\nlatitude:{latitude}\nlongitude:{longitude}",reply_markup=keyboard)

@router.message(F.contact)
async def get_contact(message: types.Message):
    ism = message.contact.first_name
    familiya = message.contact.last_name if message.contact.last_name else ""
    tel = message.contact.phone_number

    await message.answer(
        f"📞 Qabul qilindi!\nIsm: {ism}\nFamiliya: {familiya}\nRaqam: {tel}",
        reply_markup=keyboard
    )

@router.message(Command("about"))
async def get_about(message:types.Message):
    await message.answer('''🤖 Bot haqida

Bu bot Shohrux tomonidan test maqsadida yaratilgan.
Bot yordamida siz /start tugmasi orqali boshlashingiz,
shuningdek telefon raqamingiz yoki joylashuvingizni yuborishingiz mumkin.

🛠️ Hozircha bot sinov bosqichida bo‘lib,
kelajakda yangi imkoniyatlar qo‘shiladi.''',reply_markup=are_you_sure_markup)


@router.message(F.text == "🤖 Bot Haqida")
async def get_about(message:types.Message):
    await message.answer('''🤖 Bot haqida

Bu bot Shohrux tomonidan test maqsadida yaratilgan.
Bot yordamida siz /start tugmasi orqali boshlashingiz,
shuningdek telefon raqamingiz yoki joylashuvingizni yuborishingiz mumkin.

🛠️ Hozircha bot sinov bosqichida bo‘lib,
kelajakda yangi imkoniyatlar qo‘shiladi.''',reply_markup=are_you_sure_markup)

@router.callback_query(F.data == "start")
async def start_callback_handler(callback: types.CallbackQuery):
    await callback.message.answer("Bot ishga tushdi. /start komandasi bajarildi.")
    await callback.answer()

@router.callback_query(F.data == "help")
async def help_callback_handler(callback: types.CallbackQuery):
    await callback.message.answer("Yordam bo‘limi. /help komandasi bajarildi.")
    await callback.answer()