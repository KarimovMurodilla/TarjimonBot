from aiogram import Bot

from app import config
from app.admin import admin_connection


bot = Bot(token=config.TOKEN, parse_mode = 'html')


async def check_subscription(user_id):
    channel_ids = admin_connection.getChannels('id')
    checked_list = []

    for i in channel_ids:
        response = await bot.get_chat_member(i, user_id)
        if not response.is_chat_member():
            checked_list.append(False)

        else:
            checked_list.append(True)

    if False not in checked_list:
        return True

    else:
        return False