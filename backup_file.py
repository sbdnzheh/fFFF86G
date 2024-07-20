import re
import os
import requests
from pyrogram import Client
from pyrogram.types import Message
from plugins.sudos import restart


def download_to_file(url, file_path):
    r = requests.get(url, allow_redirects=True)
    open(file_path, 'wb').write(r.content)


async def get_backup(c: Client, m: Message):
    await c.send_document(m.chat.id, "theo.db", reply_to_message_id=m.id)


async def get_backup2(c: Client, m: Message):
    await c.send_document(m.chat.id, "theo2.db", reply_to_message_id=m.id)


async def upper_backup(c: Client, m: Message):
    if re.match("^theo\.db$", str(m.reply_to_message.document.file_name)):
        await c.download_media(m.reply_to_message, file_name="./theo.db")
        os.chmod('theo.db', 0o0777)
        await m.reply_text("◍ تم رفع النسخه الاحتياطيه الاساسيه\n√", reply_to_message_id=m.id)
        await restart(c, m)
