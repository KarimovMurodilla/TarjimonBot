from aiogram import types


def getAdminPanel():
	admin_panel = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
	add_channel = types.KeyboardButton("➕ Kanal qo'shish")
	del_channel = types.KeyboardButton("➖ Kanal o'chirish")
	channel_list = types.KeyboardButton("📜 Kanallar ro'yhati")
	change_message = types.KeyboardButton("🔄 Matn almashtirish")
	stat = types.KeyboardButton("📊 Statistika")
	admin_panel.add(add_channel, del_channel)
	admin_panel.add(channel_list)
	admin_panel.add(change_message)
	admin_panel.add(stat)

	return admin_panel


def getCancelBtn():
	cancel_btn = types.ReplyKeyboardMarkup(resize_keyboard = True)
	cancel = types.KeyboardButton("❌ Bekor qilish")
	cancel_btn.add(cancel)

	return cancel_btn
