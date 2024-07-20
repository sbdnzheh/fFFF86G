import random
from pyrogram import Client, filters
from pyrogram.types import Message
from config import prefix
from utils import http


@Client.on_message(filters.command("coub", prefix))
async def coub(c: Client, m: Message):
    text = m.text[6:]
    r = await http.get("https://coub.com/api/v2/search/coubs",
                       params=dict(q=text))
    rjson = r.json()
    try:
        content = random.choice(rjson["coubs"])
        links = content["permalink"]
        title = content["title"]
    except IndexError as e:
        await m.reply_text(f"{e}")
    else:
        await m.reply_text(f"**[{title}](https://coub.com/v/{links})**")
