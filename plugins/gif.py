import logging
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from config import TENOR_API_KEY, prefix
from utils import http

if not TENOR_API_KEY:
    logging.warning(f"[{__name__}] You need to fill TENOR_API_KEY in your config file in order to use this plugin.")


@Client.on_message(filters.command("gif", prefix))
async def gif(c: Client, m: Message):
    if len(m.command) == 1:
        return await m.reply_text("**الاستخدام:** `/gif` مصطلح البحث - يرسل GIF عشوائيا من نتائج البحث.", parse_mode=enums.ParseMode.MARKDOWN)

    text = m.text.split(maxsplit=1)[1]
    r = await http.get("https://api.tenor.com/v1/random",
                       params=dict(q=text, key=TENOR_API_KEY, limit=1))
    rjson = r.json()
    if rjson["results"]:
        res = rjson["results"][0]["media"][0]["mediumgif"]["url"]
        await m.reply_animation(res)
    else:
        await m.reply_text("لا توجد نتائج.")
