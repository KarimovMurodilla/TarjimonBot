from aiogram import Bot, Dispatcher, types

from app.admin import admin_buttons
from app import config


bot = Bot(token=config.TOKEN, parse_mode = 'html')


async def cmd_admin(message: types.Message):
    user_id = message.from_user.id

    await message.answer(
        "Admin panelga hush kelibsiz",
            reply_markup = admin_buttons.getAdminPanel())


def register_admin_cmd_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_admin, chat_id = config.ADMINS, commands = 'admin', state="*")
