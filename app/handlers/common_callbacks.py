from aiogram import Bot, Dispatcher, types
from app import config, connection, buttons

from app.subscription.subscription import check_subscription
from aiogram.utils.exceptions import MessageNotModified


bot = Bot(token=config.TOKEN, parse_mode = 'html')


def fast_answer(func):
	async def wrapper(c: types.CallbackQuery):
		await c.answer()
		
		return 	await func(c)
	return wrapper


async def callback_subscribed(c: types.CallbackQuery):
	user_id = c.from_user.id

	if not await check_subscription(user_id):
		await c.answer("Kanalga obuna bo'lmagansiz!", show_alert = True)

	else:
		await c.message.delete()
		await c.message.answer(
			"<b>Xush kelibsiz</b>\n\n" 
            "💥 @tarjimon_ebot - <b>shaxsiy tarjimoningiz</b>",
                reply_markup = buttons.changeLang()
			)



@fast_answer
async def callback_from_lang(c: types.CallbackQuery):
	lang = c.data[4:]
	user_id = c.from_user.id

	connection.setLang(is_from = lang, user_id = user_id)
	try:
		await bot.edit_message_reply_markup(
				chat_id = c.from_user.id, 
				message_id = c.message.message_id,
				reply_markup = buttons.langList(user_id))
	
	except MessageNotModified:
		pass


@fast_answer
async def callback_to_lang(c: types.CallbackQuery):
	lang = c.data[2:]
	user_id = c.from_user.id

	connection.setLang(is_to = lang, user_id = user_id)
	await bot.edit_message_reply_markup(
			chat_id = c.from_user.id, 
			message_id = c.message.message_id,
			reply_markup = buttons.langList(user_id))



def register_callback_handlers(dp: Dispatcher):
	dp.register_callback_query_handler(callback_subscribed, lambda c: c.data == 'subscribed')

	dp.register_callback_query_handler(callback_from_lang, lambda c: c.data.startswith('from'))
	dp.register_callback_query_handler(callback_to_lang, lambda c: c.data.startswith('to'))
