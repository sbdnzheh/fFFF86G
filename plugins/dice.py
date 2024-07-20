from pyrogram import Client, filters
from pyrogram.types import Message
from config import prefix


@Client.on_message(filters.command(["dice", "dados"], prefix))
async def dice(c: Client, m: Message):
    dicen = await c.send_dice(m.chat.id, reply_to_message_id=m.id)
    await dicen.reply_text(f"🎲 توقفت النغمة عند العدد: {dicen.dice.value}", quote=True)
