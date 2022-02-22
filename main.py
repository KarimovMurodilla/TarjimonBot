import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from app.config import TOKEN

from app.admin.admin_commands import register_admin_cmd_handlers
from app.admin.admin_panel import register_admin_panel_handlers

from app.handlers.common_commands import register_cmd_handlers
from app.handlers.common_answers import register_text_handlers
from app.handlers.common_callbacks import register_callback_handlers




async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Botni ishga tushirish")
    ]
    await bot.set_my_commands(commands)


async def main():
	logging.basicConfig(level=logging.INFO)

	storage = MemoryStorage()
	bot = Bot(token=TOKEN, parse_mode = 'html')
	dp = Dispatcher(bot, storage = storage)
	
	register_admin_cmd_handlers(dp)
	register_admin_panel_handlers(dp)

	register_cmd_handlers(dp)
	register_text_handlers(dp)
	register_callback_handlers(dp)



	await set_commands(bot)

	await dp.start_polling()



if __name__ == '__main__':
	asyncio.run(main())