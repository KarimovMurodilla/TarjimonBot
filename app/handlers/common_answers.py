from googletrans import Translator
from aiogram import Bot, Dispatcher, types
from app import buttons, config, connection
from aiogram.utils.markdown import hlink

from app.subscription.subscription import check_subscription
from app.admin import admin_connection

translator = Translator()


bot = Bot(token=config.TOKEN, parse_mode = 'html')


async def send_lang_list(message: types.Message):
    user_id = message.from_user.id

    if not await check_subscription(user_id):
        text = admin_connection.getSubscriptionText()[0]
        await message.answer(text, reply_markup = buttons.link_btns())

    else:
        await message.answer(
            "1) <b>Chap tomonda siz yuborgan xabar tili joylashgan</b> (Tilni tanlang - uning uchun chap tamondagi tugmani bosing)\n\n"
            "2) <b>O'ng tomonda tarjima qilinadigan til mavjud.</b> (Tilni tanlang - uning o'ng tomonidagi tugmani bosing)\n\n"
            "3) Tarjima uchun matnni kiriting",
                reply_markup = buttons.langList(message.from_user.id))
        await message.answer("❗️ Tarjima uchun matnni kiriting ❗️")


async def send_translate(message: types.Message):
    user_id = message.from_user.id

    if not await check_subscription(user_id):
        await message.answer("Iltimos avval kanallarga a'zo bo'ling", reply_markup = buttons.link_btns())

    else:
        # try:
        src = connection.getUser(user_id)[1]
        dest = connection.getUser(user_id)[2]

        result = translator.translate(message.text, src=src, dest=dest).text

        await message.answer(result)
        # except:
        #     await message.answer("Iltimos, avval tarjima qilinadigan tilni tanlang:")




def register_text_handlers(dp: Dispatcher):
    dp.register_message_handler(send_lang_list, text = "✅Tarjima tilini o'zgartirish✅")
    dp.register_message_handler(send_translate)
