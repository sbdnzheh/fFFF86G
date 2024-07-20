##########
#By: @XIX_A 
##########


import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information

@Client.on_callback_query(filters.regex("^status (\\d+)$"))
async def status(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("استوري حب", callback_data="love " + str(m.from_user.id))] +
        [InlineKeyboardButton("استوري حزن", callback_data="sad " + str(m.from_user.id))],
        [InlineKeyboardButton("استوري عشوائي", callback_data="xx " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("◍ اليك قائمه الاستوريهات\n√", reply_markup=keyboard)

#########################################################################################
#########################################################################################

@Client.on_callback_query(filters.regex("^love (\\d+)$"))
async def love(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    statusvideo = [str(i) for i in range(2, 18)]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_video("https://t.me/UUSSTTAATTSS/" + random.choice(statusvideo),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_video("https://t.me/UUSSTTAATTSS/" + random.choice(statusvideo),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^sad (\\d+)$"))
async def sad(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    statusvideo = [
                "2", "3", "4"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_video("https://t.me/UUSSTTAATTSS/" + random.choice(statusvideo),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_video("https://t.me/UUSSTTAATTSS/" + random.choice(statusvideo),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^xx (\\d+)$"))
async def xx(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    statusvideo = [
                "2", "3", "4"
    ]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_video("https://t.me/UUSSTTAATTSS/" + random.choice(statusvideo),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_video("https://t.me/UUSSTTAATTSS/" + random.choice(statusvideo),
                                caption=f"By: @{get_bot_information()[1]}"),
