import datetime
import sqlite3 as sql
from app import config


with sql.connect(config.ADMIN_DB_PATH, check_same_thread=False) as con:
	cur = con.cursor()


with sql.connect(config.DB_PATH, check_same_thread=False) as con2:
	cur2 = con2.cursor()


def createTableMessages():
	cur.execute("""CREATE TABLE IF NOT EXISTS messages(
				subscription_message TEXT
				)""")
	con.commit()


def createTable():
	cur.execute("""CREATE TABLE IF NOT EXISTS channels(
				channel_id INT,
				channel_name TEXT,
				channel_url TEXT
				)""")
	con.commit()


createTable()
createTableMessages()


# ---CHANNELS---
def regChannel(channel_id, channel_name, channel_url):
	cur.execute("INSERT INTO channels (channel_id, channel_name, channel_url) VALUES (?, ?, ?)", (channel_id, channel_name, channel_url,))
	con.commit()


def getChannels(key):
	if key == 'id':
		ids = cur.execute("SELECT channel_id FROM channels").fetchall()
		channel_ids = [x[0] for x in ids]

		return channel_ids

	elif key == 'name':
		names = cur.execute("SELECT channel_name FROM channels").fetchall()
		channel_names = [x[0] for x in names]

		return channel_names

	elif key == 'url':
		urls = cur.execute("SELECT channel_url FROM channels").fetchall()
		channel_urls = [x[0] for x in urls]

		return channel_urls


def delete_channel(channel_id):
	cur.execute("DELETE FROM channels WHERE channel_id = ?", (channel_id,))
	con.commit()


def showStat(interval):
	if interval == 'all':
		users = cur2.execute("SELECT user_id FROM users").fetchall()
		return users

	elif interval == '24':
		today = datetime.datetime.today()
		yesterday = today - datetime.timedelta(days=1)
		users = cur2.execute(f"SELECT user_id FROM users WHERE date_reg BETWEEN \'{yesterday}\' AND \'{today}\'").fetchall()
		return users

	elif interval == 'month':
		today = datetime.datetime.today()
		month = today - datetime.timedelta(days=30)

		users = cur2.execute(f"SELECT user_id FROM users WHERE date_reg BETWEEN \'{month}\' AND \'{today}\'").fetchall()
		return users


# ---MESSAGES---
def setSubscriptionMessage(text):
	cur.execute("UPDATE messages SET subscription_message = ?", (text,))
	con.commit()


def getSubscriptionText():
	text = cur.execute("SELECT subscription_message FROM messages").fetchone()
	return text