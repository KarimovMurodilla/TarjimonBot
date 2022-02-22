from aiogram import Bot, Dispatcher, types

from app import buttons, config, connection
from app.subscription.subscription import check_subscription


bot = Bot(token=config.TOKEN, parse_mode = 'html')


async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    connection.checkUser(user_id)

    if not await check_subscription(user_id):
        await message.answer("Iltimos avval kanallarga a'zo bo'ling", reply_markup = buttons.link_btns())

    else:
        await message.answer(
            "<b>Xush kelibsiz</b>\n\n" 
            "💥 @tarjimon_ebot - <b>shaxsiy tarjimoningiz</b>",
                reply_markup = buttons.changeLang()
                )


def register_cmd_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands = 'start', state="*")
