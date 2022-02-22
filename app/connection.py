import datetime
import sqlite3 as sql

from app import config


with sql.connect(config.DB_PATH, check_same_thread=False) as con:
	cur = con.cursor()


def createTable():
	cur.execute("""CREATE TABLE IF NOT EXISTS users(
				user_id INT,
				from_lang TEXT,
				to_lang TEXT,
				date_reg TIMESTAMP
				)""")
	con.commit()


createTable()


def checkUser(user_id):
	user = cur.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchone()

	if not user:
		cur.execute("INSERT INTO users (user_id, date_reg) VALUES (?, ?)", (user_id, datetime.datetime.today()))
		con.commit()

	return user


def setLang(is_from = None, is_to = None, user_id = None):
	if is_from:
		cur.execute("UPDATE users SET from_lang = ? WHERE user_id = ?", (is_from, user_id,))
		con.commit()

	elif is_to:
		cur.execute("UPDATE users SET to_lang = ? WHERE user_id = ?", (is_to, user_id,))
		con.commit()


def getUser(user_id):
	user = cur.execute("SELECT * FROM users WHERE user_id = ?", (user_id,)).fetchone()

	return user


def checkIndicator(user_id, language):
	if language.startswith("from"):
		lang = cur.execute("SELECT * FROM users WHERE user_id = ? AND from_lang = ?", (user_id, language[4:],)).fetchone()

		if lang:
			return '✅'

		else:
			return ''

	elif language.startswith("to"):
		lang = cur.execute("SELECT * FROM users WHERE user_id = ? AND to_lang = ?", (user_id, language[2:],)).fetchone()
		
		if lang:
			return '✅'

		else:
			return ''