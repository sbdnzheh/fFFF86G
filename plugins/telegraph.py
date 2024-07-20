import os
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from config import prefix
from telegraph import upload_file


@Client.on_message(filters.command("تليجراف", ""), group=54)
async def telegraph(c: Client, m: Message):
    replied = m.reply_to_message
    if not replied:
        return await m.reply("Please Reply to Photo or Video")
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (replied.video and replied.video.file_name.endswith(".mp4") and replied.video.file_size <= 5242880)
        or (replied.document and replied.document.file_name.endswith((".jpg", ".jpeg", ".png", ".gif", ".mp4")) and replied.document.file_size <= 5242880)):
        return await m.reply("◍ عذرا هذا العنصر غير مدعوم\n√")
    download_location = await c.download_media(message=m.reply_to_message,file_name="root/downloads/")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await m.reply(message, text=document)
    else:
        await m.reply(f"`https://telegra.ph{response[0]}`", parse_mode=enums.ParseMode.MARKDOWN)
    finally:
        os.remove(download_location)
