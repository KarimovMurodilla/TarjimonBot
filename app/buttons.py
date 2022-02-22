from aiogram import types
from app.connection import checkIndicator
from app.admin import admin_connection


def changeLang():
	btn = types.ReplyKeyboardMarkup(resize_keyboard = True)
	btn_change = types.KeyboardButton("✅Tarjima tilini o'zgartirish✅")
	btn.add(btn_change)

	return btn


def langList(user_id):
	lang_btns = types.InlineKeyboardMarkup(row_width = 2)

	uz = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromuz')} 🇺🇿 O'zbek", callback_data = "fromuz")
	en = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromen')} 🇬🇧 English", callback_data = "fromen")
	ru = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromru')} 🇷🇺 Русский", callback_data = "fromru")
	kor = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromko')} 🇰🇷 Korean", callback_data = "fromko")
	ar = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromar')} 🇸🇦 Arabic", callback_data = "fromar")
	chn = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromzh-cn')} 🇨🇳 Chinese", callback_data = "fromzh-cn")
	kz = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromkk')} 🇰🇿 Kazakh", callback_data = "fromkk")
	tj = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromtg')} 🇹🇯 Tajik", callback_data = "fromtg")
	tur = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromtr')} 🇹🇷 Turkish", callback_data = "fromtr")
	fr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromfr')} 🇫🇷 French", callback_data = "fromfr")
	sp = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromes')} 🇪🇸 Spanish", callback_data = "fromes")
	jp = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromja')} 🇯🇵 Japanese", callback_data = "fromja")
	gr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromde')} 🇩🇪 German", callback_data = "fromde")
	it = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromit')} 🇮🇹 Italian", callback_data = "fromit")
	ukr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromuk')} 🇺🇦 Ukraine", callback_data = "fromuk")
	por = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'frompt')} 🇵🇹 Portugal", callback_data = "frompt")
	hind = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromhi')} 🇮🇳 Hindi", callback_data = "fromhi")

	touzb = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'touz')} 🇺🇿 O'zbek", callback_data = "touz")
	toeng = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toen')} 🇬🇧 English", callback_data = "toen")
	torus = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toru')} 🇷🇺 Русский", callback_data = "toru")
	tokor = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toko')} 🇰🇷 Korean", callback_data = "toko")
	toara = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toar')} 🇸🇦 Arabic", callback_data = "toar")
	tochn = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tozh-cn')} 🇨🇳 Chinese", callback_data = "tozh-cn")
	tokz = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tokk')} 🇰🇿 Kazakh", callback_data = "tokk")
	totj = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'totg')} 🇹🇯 Tajik", callback_data = "totg")
	totur = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'totr')} 🇹🇷 Turkish", callback_data = "totr")
	tofra = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tofr')} 🇫🇷 French", callback_data = "tofr")
	tosp = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toes')} 🇪🇸 Spain", callback_data = "toes")
	tojp = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toja')} 🇯🇵 Japanese", callback_data = "toja")
	togr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tode')} 🇩🇪 German", callback_data = "tode")
	toita = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toit')} 🇮🇹 Italian", callback_data = "toit")
	toukr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'touk')} 🇺🇦 Ukraine", callback_data = "touk")
	topor = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'topt')} 🇵🇹 Portugal", callback_data = "topt")
	tohind = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tohi')} 🇮🇳 Hindi", callback_data = "tohi")

	lang_btns.add(
		uz, touzb,
		en, toeng,
		ru, torus,
		kor, tokor,
		ar, toara,
		chn, tochn,
		kz, tokz,
		tj, totj,
		tur, totur,
		fr, tofra,
		sp, tosp,
		jp, tojp,
		gr, togr,
		it, toita,
		ukr, toukr,
		por, topor,
		hind, tohind
		)

	return lang_btns


def link_btns(admin_side = False):
	names = admin_connection.getChannels('name')
	urls = admin_connection.getChannels('url')

	url_btns = types.InlineKeyboardMarkup(row_width=1)
	btn_subscribed = types.InlineKeyboardButton(text = "✅ Tekshirish", callback_data = 'subscribed')
	for n, u in zip(names, urls):
		url_btns.add(types.InlineKeyboardButton(text = n, url = u))

	if not admin_side:
		url_btns.add(btn_subscribed)


	return url_btns
