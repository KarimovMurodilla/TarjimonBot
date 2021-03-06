from aiogram import types
from app.connection import checkIndicator
from app.admin import admin_connection


def changeLang():
	btn = types.ReplyKeyboardMarkup(resize_keyboard = True)
	btn_change = types.KeyboardButton("โTarjima tilini o'zgartirishโ")
	btn.add(btn_change)

	return btn


def langList(user_id):
	lang_btns = types.InlineKeyboardMarkup(row_width = 2)

	uz = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromuz')} ๐บ๐ฟ O'zbek", callback_data = "fromuz")
	en = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromen')} ๐ฌ๐ง English", callback_data = "fromen")
	ru = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromru')} ๐ท๐บ ะ ัััะบะธะน", callback_data = "fromru")
	kor = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromko')} ๐ฐ๐ท Korean", callback_data = "fromko")
	ar = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromar')} ๐ธ๐ฆ Arabic", callback_data = "fromar")
	chn = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromzh-cn')} ๐จ๐ณ Chinese", callback_data = "fromzh-cn")
	kz = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromkk')} ๐ฐ๐ฟ Kazakh", callback_data = "fromkk")
	tj = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromtg')} ๐น๐ฏ Tajik", callback_data = "fromtg")
	tur = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromtr')} ๐น๐ท Turkish", callback_data = "fromtr")
	fr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromfr')} ๐ซ๐ท French", callback_data = "fromfr")
	sp = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromes')} ๐ช๐ธ Spanish", callback_data = "fromes")
	jp = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromja')} ๐ฏ๐ต Japanese", callback_data = "fromja")
	gr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromde')} ๐ฉ๐ช German", callback_data = "fromde")
	it = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromit')} ๐ฎ๐น Italian", callback_data = "fromit")
	ukr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromuk')} ๐บ๐ฆ Ukraine", callback_data = "fromuk")
	por = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'frompt')} ๐ต๐น Portugal", callback_data = "frompt")
	hind = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'fromhi')} ๐ฎ๐ณ Hindi", callback_data = "fromhi")

	touzb = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'touz')} ๐บ๐ฟ O'zbek", callback_data = "touz")
	toeng = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toen')} ๐ฌ๐ง English", callback_data = "toen")
	torus = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toru')} ๐ท๐บ ะ ัััะบะธะน", callback_data = "toru")
	tokor = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toko')} ๐ฐ๐ท Korean", callback_data = "toko")
	toara = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toar')} ๐ธ๐ฆ Arabic", callback_data = "toar")
	tochn = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tozh-cn')} ๐จ๐ณ Chinese", callback_data = "tozh-cn")
	tokz = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tokk')} ๐ฐ๐ฟ Kazakh", callback_data = "tokk")
	totj = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'totg')} ๐น๐ฏ Tajik", callback_data = "totg")
	totur = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'totr')} ๐น๐ท Turkish", callback_data = "totr")
	tofra = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tofr')} ๐ซ๐ท French", callback_data = "tofr")
	tosp = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toes')} ๐ช๐ธ Spain", callback_data = "toes")
	tojp = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toja')} ๐ฏ๐ต Japanese", callback_data = "toja")
	togr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tode')} ๐ฉ๐ช German", callback_data = "tode")
	toita = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'toit')} ๐ฎ๐น Italian", callback_data = "toit")
	toukr = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'touk')} ๐บ๐ฆ Ukraine", callback_data = "touk")
	topor = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'topt')} ๐ต๐น Portugal", callback_data = "topt")
	tohind = types.InlineKeyboardButton(text = f"{checkIndicator(user_id, 'tohi')} ๐ฎ๐ณ Hindi", callback_data = "tohi")

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
	btn_subscribed = types.InlineKeyboardButton(text = "โ Tekshirish", callback_data = 'subscribed')
	for n, u in zip(names, urls):
		url_btns.add(types.InlineKeyboardButton(text = n, url = u))

	if not admin_side:
		url_btns.add(btn_subscribed)


	return url_btns
