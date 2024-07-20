##########
#By: @XIX_A 
##########


import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from config import get_bot_information

@Client.on_callback_query(filters.regex("^rmaziat (\\d+)$"))
async def rmaziat(c: Client, m: Message):
    global mid
    mid = m.id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("رمزيات بنات", callback_data="g " + str(m.from_user.id))] +
        [InlineKeyboardButton("رمزيات شباب", callback_data="b " + str(m.from_user.id))],
        [InlineKeyboardButton("صور انمي", callback_data="a " + str(m.from_user.id))],

        [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅", url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],

    ])
    await m.reply_text("◍ اليك قائمه الرمزيات\n√", reply_markup=keyboard)

#########################################################################################
#########################################################################################

@Client.on_callback_query(filters.regex("^b (\\d+)$"))
async def b(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    Rmaziatphoto = [str(i) for i in range(2, 213)]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_photo("https://t.me/UGTRRT/" + random.choice(Rmaziatphoto),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_photo("https://t.me/UGTRRT/" + random.choice(Rmaziatphoto),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^g (\\d+)$"))
async def g(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    Rmaziatphoto = [str(i) for i in range(2, 104)]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_photo("https://t.me/UTFGTT/" + random.choice(Rmaziatphoto),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_photo("https://t.me/UTFGTT/" + random.choice(Rmaziatphoto),
                                caption=f"By: @{get_bot_information()[1]}"),


@Client.on_callback_query(filters.regex("^a (\\d+)$"))
async def a(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    Rmaziatphoto = [str(i) for i in range(152, 467)]
    if m.message.reply_to_message:
        await m.message.reply_to_message.reply_photo("https://t.me/DDUUCCUU/" + random.choice(Rmaziatphoto),
                                caption=f"By: @{get_bot_information()[1]}"),
    else:
        await m.message.reply_photo("https://t.me/DDUUCCUU/" + random.choice(Rmaziatphoto),
                                caption=f"By: @{get_bot_information()[1]}"),
