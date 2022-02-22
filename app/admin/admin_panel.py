import time
import datetime
from googletrans import Translator

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.exceptions import BotBlocked, TelegramAPIError

from app.admin import admin_buttons, admin_connection
from app import buttons, config, connection
from app.subscription.subscription import check_subscription


bot = Bot(token=config.TOKEN, parse_mode = 'html')


class AddChannel(StatesGroup):
	get_id = State()
	get_name = State()
	get_url = State()


class DelChannel(StatesGroup):
	get_channel_id = State()


class ChangeMessage(StatesGroup):
	get_text = State()

async def cancel(message: types.Message, state: FSMContext):
	await message.answer("✅ Bekor qilindi", reply_markup = admin_buttons.getAdminPanel())
	await state.finish()


# ---KANAL QO'SHISH---
async def add_channel(message: types.Message, state: FSMContext):
	await AddChannel.get_id.set()
	await message.answer("Kanal idsini jonating", reply_markup = admin_buttons.getCancelBtn())


async def process_get_id(message: types.Message, state: FSMContext):
	user_id = message.from_user.id
	channel_id = message.text

	if message.text[1:].isdigit() and message.text.startswith('-'):
		try:
			response = await bot.get_chat_member(channel_id, user_id)
			
			async with state.proxy() as data:
				data['channel_id'] = channel_id

				await AddChannel.next()
				await message.answer("Kanal nomini jonating")
		except:
			await message.answer("Avval botni shu kanalga admin qiling!")

	else:
		await message.answer("Bu kanal idsi emas!")


async def process_get_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['channel_name'] = message.text
		
		await AddChannel.next()
		await message.answer("Kanal linkini jonating")


async def process_get_url(message: types.Message, state: FSMContext):
	if message.text.startswith("http") or message.text.startswith("t.me"):
		async with state.proxy() as data:
			channel_url = message.text
			channel_id = data['channel_id']
			channel_name = data['channel_name']

			admin_connection.regChannel(channel_id, channel_name, channel_url)

			await message.answer("✅ Kanal muvaffaqiyatli saqlandi", reply_markup = admin_buttons.getAdminPanel())

		await state.finish()
	
	else:
		await message.answer("Bunday url to'g'ri kelmaydi!")


# ---KANAL O'CHIRISH---
async def del_channel(message: types.Message, state: FSMContext):
	await DelChannel.get_channel_id.set()
	await message.answer("Kanal idsini jonating", reply_markup = admin_buttons.getCancelBtn())


async def process_del_channel(message: types.Message, state: FSMContext):
	try:
		channel_id = int(message.text)
		if channel_id in admin_connection.getChannels('id'):
			admin_connection.delete_channel(channel_id)
			await message.answer("✅ Kanal muvaffaqiyatli o'chirildi", reply_markup = admin_buttons.getAdminPanel())
			await state.finish()

		else:
			await message.answer("Bunday kanal bazada mavjud emas!")
	
	except:
		await message.answer("Bunday kanal bazada mavjud emas!")


# ---Majburiy kanallarni royhati---
async def get_channel_list(message: types.Message):
	await message.answer("Kannallar ro'yhati:", reply_markup = buttons.link_btns(admin_side = True))


# ---Matnni almashtirish---
async def get_change_message(message: types.Message):
	await ChangeMessage.get_text.set()
	await message.answer("Matn kiriting:", reply_markup = admin_buttons.getCancelBtn())


async def process_get_text(message: types.Message, state: FSMContext):
	admin_connection.setSubscriptionMessage(message.text)

	await message.answer("✅ Matn muvaffaqiyatli o'zgartirildi", reply_markup = admin_buttons.getAdminPanel())
	await state.finish()


# ---STATISTIKA---
async def statistics(message: types.Message):
	all_users = admin_connection.showStat('all')
	today = admin_connection.showStat('24')
	month = admin_connection.showStat('month')

	await message.answer(
		f"🧑🏻‍💻 Botdagi obunachilar: <code>{len(all_users)}</code> ta\n\n"

		f"Oxirgi 24 soatda: <code>{len(today)}</code> ta obunachi qo'shildi\n"
		f"Oxirgi 1 oyda: <code>{len(month)}</code> ta obunachi qo'shildi\n\n"

		"📊 @tarjimon_ebot statistikasi"
		)


# ---SENDING---
async def sending(message: types.Message):
	users = admin_connection.showStat('all')
	ids = [x[0] for x in users]

	all_users = 0
	actives = 0
	blocked = 0

	for i in ids:
		all_users += 1

		try:
			await bot.send_chat_action(i, action = 'typing')
			# await message.send_copy(i, config.CHANNEL_POSTED_ID)
			actives += 1


		except BotBlocked:
			blocked += 1
			continue
		
		except TelegramAPIError as t:
			time.sleep(0.1)
			continue

		else:
			time.sleep(0.1)
			continue

	
	for n in config.ADMINS:
		await bot.send_message(
			chat_id = n,
			text = f"Jo'natildi: <code>{all_users}</code>\n"
				   f"Yetib bordi: <code>{actives}</code>"
			)


def register_admin_panel_handlers(dp: Dispatcher):
	dp.register_message_handler(cancel, chat_id = config.ADMINS, text = '❌ Bekor qilish', state = '*')

	dp.register_message_handler(add_channel, chat_id = config.ADMINS, text = "➕ Kanal qo'shish", state = '*')
	dp.register_message_handler(process_get_id, chat_id = config.ADMINS, state = AddChannel.get_id)
	dp.register_message_handler(process_get_name, chat_id = config.ADMINS, state = AddChannel.get_name)
	dp.register_message_handler(process_get_url, chat_id = config.ADMINS, state = AddChannel.get_url)

	dp.register_message_handler(del_channel, chat_id = config.ADMINS, text = "➖ Kanal o'chirish", state = '*')
	dp.register_message_handler(process_del_channel, chat_id = config.ADMINS, state = DelChannel.get_channel_id)

	dp.register_message_handler(get_channel_list, chat_id = config.ADMINS, text = "📜 Kanallar ro'yhati", state = '*')

	dp.register_message_handler(get_change_message, chat_id = config.ADMINS, text = "🔄 Matn almashtirish", state = '*')
	dp.register_message_handler(process_get_text, chat_id = config.ADMINS, state = ChangeMessage.get_text)

	dp.register_message_handler(statistics, chat_id = config.ADMINS, text = '📊 Statistika', state = '*')

	# dp.register_channel_post_handler(sending, chat_id = config.CHANNEL_POSTED_ID, content_types = 'any')


