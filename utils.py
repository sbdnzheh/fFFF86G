import time, html, inspect, os.path, httpx, sqlite3
from datetime import datetime, timedelta
from pyrogram import Client, enums
from pyrogram.types import Message, ChatPrivileges
from typing import Union, Optional
from functools import wraps, partial

db = sqlite3.connect("dream.db")
dbc = db.cursor()

dbc.execute("CREATE TABLE IF NOT EXISTS was_restarted_at (chat_id INTEGER, message_id INTEGER)")
db.commit()

def set_restarted(chat_id, message_id):
    dbc.execute("INSERT INTO was_restarted_at VALUES (?, ?)", (chat_id, message_id))
    db.commit()


def del_restarted():
    dbc.execute("DELETE FROM was_restarted_at")
    db.commit()


def get_restarted():
    dbc.execute("SELECT * FROM was_restarted_at")
    return dbc.fetchone()


http = httpx.AsyncClient(http2=True)

async def time_extract(m: Message, time: str) -> Optional[datetime]:
    if time[-1] not in ["m", "h", "d"]:
        await m.reply_text("Invalid time format. Use 'h'/'m'/'d' ")
        return None
    unit = time[-1]
    num = time[:-1]
    if not num.isdigit():
        await m.reply_text("Invalid Amount specified")
        return None
    if unit == "m":
        return datetime.now() + timedelta(minutes=int(num))
    if unit == "h":
        return datetime.now() + timedelta(hours=int(num))
    if unit == "d":
        return datetime.now() + timedelta(days=int(num))

    return None


def html_user(name: str, user_id: int):
    name = html.escape(name)
    _html = f"<a href='tg://user?id={user_id}'>{name}</a>"
    return _html
