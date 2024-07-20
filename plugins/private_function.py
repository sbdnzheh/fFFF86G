import random
import re
import requests
from pyrogram import filters, Client, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
from backup_file import get_backup, upper_backup, get_backup2
from config import super_sudoers, get_bot_information
from database import set_db_wait, get_db_gban, get_db_gmute, get_db_greply, get_db_botname, \
    del_db_gmuteall, del_db_gbanall, del_db_banallall, del_db_muteallall, del_db_meendafnyallall, \
    del_db_mycontactallall, del_db_mypointgameallall, del_db_mymessageallall, drop_db_replygroup, drop_db_locktext, \
    drop_db_wait, drop_db_waitq, get_db_priban, del_db_pribanall, drop_db_pribanallall, del_db_general_rtball
from plugins.abrag import abrag
from plugins.aflam import aflamAR
from plugins.cartoon import cartoon
from plugins.commands import command
from plugins.developer import developersrep, developersuser, undevelopersrep, undeveloperuser, seconddevelopersrep, \
    seconddevelopersuser, secondundevelopersrep, secondundeveloperuser
from plugins.games import games
from plugins.general import replay_global_test, gunbanuser, gunbanrep, gmuteuser, gmuterep, gbanuser, gbanrep
from plugins.ids import ids_private
from plugins.keyboard_private import *
from plugins.music import music
from plugins.private_ban import privbanrep, privbanuser, privunbanrep, privunbanuser, priban_user_test
from plugins.quran import quran
from plugins.ghnely import ghnely
from plugins.rmaziat import rmaziat
from plugins.reply import addgeneralrep, delgeneralrep, namebot, omrk, echo_text, allreply_for_bot, say_text
from plugins.rtp_function import *
from plugins.rwayat import rwaiat
from plugins.status import status
from plugins.sudos import test_speed, upgrade, restart
from plugins.wait import wait_all
from plugins.weather import weather
from plugins.youtube import youtube_main


@Client.on_message(filters.private & ~filters.regex("^/") & ~filters.me)
@Client.on_edited_message(filters.private & ~filters.regex("^/") & ~filters.me)
async def baseprivate(c: Client, m: Message):
    global qrwp


########################################################################################################################
########################################################################################################################

    if priban_user_test(m):
        await m.reply_text("◍ قام المطور بحظرك من خاص البوت\n√")
        return


########################################################################################################################
########################################################################################################################

    await wait_all(c, m)


########################################################################################################################
########################################################################################################################

    if replay_global_test(m):
        for rp in get_db_greply():
            if m.text == rp[0]:
                if re.findall("\.png$", rp[1]):
                    reptxttypy = rp[1].split(".png")
                    await m.reply_photo(reptxttypy[0])
                else:
                    if re.findall("\.webp$", rp[1]):
                        reptxttypy = rp[1].split(".webp")
                        await m.reply_sticker(reptxttypy[0])
                    else:
                        if re.findall("\.gif$", rp[1]):
                            reptxttypy = rp[1].split(".gif")
                            await m.reply_animation(reptxttypy[0])
                        else:
                            if re.findall("\.pdf$", rp[1]):
                                reptxttypy = rp[1].split(".pdf")
                                await m.reply_document(reptxttypy[0])
                            else:
                                if re.findall("\.mp3$", rp[1]):
                                    reptxttypy = rp[1].split(".mp3")
                                    await m.reply_audio(reptxttypy[0])
                                else:
                                    if re.findall("\.ogg$", rp[1]):
                                        reptxttypy = rp[1].split(".ogg")
                                        await m.reply_voice(reptxttypy[0])
                                    else:
                                        await m.reply_text(rp[1], parse_mode=enums.ParseMode.MARKDOWN)


########################################################################################################################
########################################################################################################################

    if m.text == "رفع مطور" and m.reply_to_message:
        if secsudo(m):
            await developersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^رفع مطور @(.*)$", str(m.text)) or re.match("^رفع مطور (\\d+)$", str(m.text)):
        if secsudo(m):
            await developersuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تنزيل مطور" and m.reply_to_message:
        if secsudo(m):
            await undevelopersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^تنزيل مطور @(.*)$", str(m.text)) or re.match("^تنزيل مطور (\\d+)$", str(m.text)):
        if secsudo(m):
            await undeveloperuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المطورين":
        if sudo2(m):
            try:
                lang = get_db_general_rtb("developer")
                n = await c.get_users(sudoers[0])
                if lang is None:
                    await m.reply_text(f"◍ [𝗦𝗼𝘂𝗿𝗰𝗲 𝗻𝗼𝘂𝗿](tg://user?id={super_sudoers[0]})\n" +
                                       f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n"
                                       "لا يوجد مطورين مرفوعين\n√",
                                       parse_mode=enums.ParseMode.MARKDOWN)
                else:
                    t = "\n◍ قائمة المطورين \n≪━━━━━━━━━━━━━≫\n" + f"◍ [𝗦𝗼𝘂𝗿𝗰𝗲 𝗻𝗼𝘂𝗿](tg://user?id={super_sudoers[0]})\n" + f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n√"
                    for row in lang:
                        t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                    await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            except Exception as e:
                print("developer " + str(e))

        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المطورين":
        if secsudo(m):
            del_db_general_rtball("developer")
            developer.clear()
            await m.reply_text("◍ تم حذف المطورين\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "رفع مطور ثانوي" and m.reply_to_message:
        if sudo(m):
            await seconddevelopersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^رفع مطور ثانوي @(.*)$", str(m.text)) or re.match("^رفع مطور ثانوي (\\d+)$", str(m.text)):
        if sudo(m):
            await seconddevelopersuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "رفع مطور ثانوي" and m.reply_to_message:
        if sudo(m):
            await seconddevelopersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^رفع مطور ثانوي @(.*)$", str(m.text)) or re.match("^رفع مطور ثانوي (\\d+)$", str(m.text)):
        if sudo(m):
            await seconddevelopersuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تنزيل مطور ثانوي" and m.reply_to_message:
        if sudo(m):
            await secondundevelopersrep(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^تنزيل مطور ثانوي @(.*)$", str(m.text)) or re.match("^تنزيل مطور ثانوي (\\d+)$", str(m.text)):
        if sudo(m):
            await secondundeveloperuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المطورين الثانويين" or m.text == "المطورين الثانوين":
        if sudo2(m):
            try:
                lang = get_db_general_rtb("secdeveloper")
                n = await c.get_users(sudoers[0])
                if lang is None:
                    await m.reply_text(f"◍ [𝗦𝗼𝘂𝗿𝗰𝗲 𝗻𝗼𝘂𝗿](tg://user?id={super_sudoers[0]})\n" +
                                       f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n√"
                                       "لا يوجد مطورين ثانويين مرفوعين\n√",
                                       parse_mode=enums.ParseMode.MARKDOWN)
                else:
                    t = "\n◍ قائمة المطورين الثانويين \n≪━━━━━━━𝗻𝗼𝘂𝗿━━━━━━≫\n" + f"◍ [𝗦𝗼𝘂𝗿𝗰𝗲 𝗻𝗼𝘂𝗿](tg://user?id={super_sudoers[0]})\n" + f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n√"
                    for row in lang:
                        t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                    await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            except Exception as e:
                print("second developer " + str(e))

        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المطورين الثانويين" or m.text == "حذف الثانويين" or m.text == "حذف الثانوين" or m.text == "حذف المطورين الثانوين":
        if sudo(m):
            del_db_general_rtball("secdeveloper")
            developer.clear()
            await m.reply_text("◍ تم حذف المطورين الثانويين\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "حظر عام" and m.reply_to_message:
        if secsudo(m):
            await gbanrep(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if re.match("^حظر عام @(.*)$", str(m.text)):
        if secsudo(m):
            await gbanuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^حظر عام (\\d+)$", str(m.text)):
        if secsudo(m):
            await gbanuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "كتم عام" and m.reply_to_message:
        if secsudo(m):
            await gmuterep(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if re.match("^كتم عام @(.*)$", str(m.text)):
        if secsudo(m):
            await gmuteuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^كتم عام (\\d+)$", str(m.text)):
        if secsudo(m):
            await gmuteuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "الغاء العام" and m.reply_to_message:
        if secsudo(m):
            await gunbanrep(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if re.match("^الغاء العام @(.*)$", str(m.text)):
        if secsudo(m):
            await gunbanuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
    if re.match("^الغاء العام (\\d+)$", str(m.text)):
        if secsudo(m):
            await gunbanuser(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المحظورين عام":
        if sudo2(m):
            lang = get_db_gban()
            if lang is None:
                await m.reply_text("◍ لايوجد محظورين عام\n√")
            else:
                t = "\n◍ قائمة المحظورين عام \n≪━━━━━━━𝗻𝗼𝘂𝗿━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المحظورين عام":
        if secsudo(m):
            del_db_gbanall()
            await m.reply_text("◍ تم حذف المحظورين عام\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المكتومين عام":
        if sudo2(m):
            lang = get_db_gmute()
            if lang is None:
                await m.reply_text("◍ لا يوجد مكتومين عام\n√")
            else:
                t = "\n◍ قائمة الكتم العام \n≪━━━━━━━𝗻𝗼𝘂𝗿━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف المكتومين عام":
        if secsudo(m):
            del_db_gmuteall()
            await m.reply_text("◍ تم حذف المكتومين عام\n√")
            return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return
            
    if m.text == "⏬ قفل الكيبورد ⏬":
        if secsudo(m):
            await m.reply_text("◍ تم قفل الكيبورد لفتحه مره اخري اضغط /start\n√", reply_markup= ReplyKeyboardRemove(selective=True))
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تفعيل التواصل ⚡️":
        if secsudo(m):
            await lock_locksendmsg_open(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تعطيل التواصل 🔰":
        if secsudo(m):
            await lock_locksendmsg_close(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "المطورين 🔱":
        if sudo2(m):
            lang = get_db_general_rtb("developer")
            n = await c.get_users(sudoers[0])
            if lang is None:
                await m.reply_text(f"◍ [𝗦𝗼𝘂𝗿𝗰𝗲 𝗻𝗼𝘂𝗿](tg://user?id={super_sudoers[0]})\n" +
                                       f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n"
                                   "لا يوجد مطورين مرفوعين\n√", parse_mode=enums.ParseMode.MARKDOWN)
            else:
                t = "\n◍ قائمة المطورين \n≪━━━━━━━𝗻𝗼𝘂𝗿━━━━━━≫\n" + f"◍ [𝗦𝗼𝘂𝗿𝗰𝗲 𝗻𝗼𝘂𝗿](tg://user?id={super_sudoers[0]})\n" + \
                    f"◍ [{n.first_name}](tg://user?id={sudoers[0]})\n\n√"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "تفعيل الاذاعه 🔔":
        if secsudo(m):
            await lock_lockbroadcast_close(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تعطيل الاذاعه 🔕":
        if secsudo(m):
            await lock_lockbroadcast_open(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تفعيل اليوتيوب ⚙️":
        if secsudo(m):
            await lock_lockgenyoutube_open(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تعطيل اليوتيوب 🛠":
        if secsudo(m):
            await lock_lockgenyoutube_close(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تفعيل المنشن @all 🎭":
        if secsudo(m):
            await lock_lockgenmnshn_open(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تعطيل المنشن @all 👩‍🎨":
        if secsudo(m):
            await lock_lockgenmnshn_close(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "اذاعه بالمجموعات 📡" or m.text == "اذاعه بالمجموعات":
        if secsudo(m):
            set_db_wait("gbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("gbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه خاص 🔊" or m.text == "اذاعه خاص":
        if secsudo(m):
            set_db_wait("ubroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("ubroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه بالتوجيه للمجموعات ⁦♻️⁩" or m.text == "اذاعه بالتوجيه للمجموعات":
        if secsudo(m):
            set_db_wait("gforwardbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("gforwardbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه بالتوجيه خاص 👤" or m.text == "اذاعه بالتوجيه خاص":
        if secsudo(m):
            set_db_wait("uforwardbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("uforwardbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه بالتثبيت 📎" or m.text == "اذاعه بالتثبيت":
        if secsudo(m):
            set_db_wait("gpinbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("gpinbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "اذاعه موجهه بالتثبيت ⁦♻️⁩" or m.text == "اذاعه موجهه بالتثبيت":
        if secsudo(m):
            set_db_wait("uforwardpinbroadcast", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
            return
        if sudo2(m):
            if await lock_lockbroadcast_test():
                set_db_wait("uforwardpinbroadcast", m.from_user.id, m.chat.id)
                await m.reply_text("◍ ارسل لى الاذاعه الان\n√")
                return
            else:
                await m.reply_text("◍ الاذاعه مقفوله من قبل المطور الاساسي\n√")
                return
        else:
            await m.reply_text("◍ هذا الامر للمطورين فقط\n√")
            return

    if m.text == "الاحصائيات 📊" or m.text == "الاحصائيات":
        await get_num_for_user_and_group(m)
        return

    if m.text == "حذف الجروبات الفيك ⚡️":
        if secsudo(m):
            await get_fact_num_group(m, c)
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return
    if m.text == "حذف الاعضاء الفيك ⚡️":
        if secsudo(m):
            await get_fact_num_user(m, c)
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "الجروبات 📢":
        if secsudo(m):
            await get_num_group(m, c)
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "المشتركين ⁦🗣️⁩":
        if secsudo(m):
            await get_num_user(m)
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "قائمه الحظر العام 🚫":
        if sudo2(m):
            lang = get_db_gban()
            if lang is None:
                await m.reply_text("◍ لايوجد محظورين عام\n√")
            else:
                t = "\n◍ قائمة المحظورين عام \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "قائمه الكتم العام 🛑":
        if sudo2(m):
            lang = get_db_gmute()
            if lang is None:
                await m.reply_text("◍ لا يوجد مكتومين عام\n√")
            else:
                t = "\n◍ قائمة الكتم العام \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "اضف رد عام 💬":
        if secsudo(m):
            await addgeneralrep(m)
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "حذف رد عام 🚫":
        if secsudo(m):
            await delgeneralrep(m)
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "الردود العامه 📝" or m.text == "الردود العامه":
        if sudo2(m):
            lang = get_db_greply()
            if lang is None:
                await m.reply_text("◍ لا توجد ردود عامه")
            else:
                t = "\n◍ قائمة الردود العامه \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"({row[0]})--->({row[1]})\n"
                await m.reply_text(t)
            return
        else:
            await m.reply_text("◍ انت لست المطور\n√")
            return

    if m.text == "ضع اسم للبوت 🤖":
        if secsudo(m):
            await namebot(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "جلب نسخه احتياطيه اساسيه 📬":
        if secsudo(m):
            await get_backup(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "جلب نسخه الردود 📬":
        if secsudo(m):
            await get_backup2(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "رفع نسخه احتياطيه ⛓" or m.text == "رفع نسخه احتياطيه" and m.reply_to_message:
        if secsudo(m):
            if m.reply_to_message.document:
                await upper_backup(c, m)
            else:
                await m.reply_text("◍ ◍ من فضلك قم باختيار الملف اولا\n√")
                return
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "معلومات السيرفر ℹ️":
        if secsudo(m):
            await get_information_server(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "سرعه السيرفر 🚀️":
        if secsudo(m):
            await test_speed(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "الاصدار ⁦⚙️⁩":
        if secsudo(m):
            await get_version_source(m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "تحديث السورس 📥":
        if secsudo(m):
            await upgrade(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return

    if m.text == "رستر البوت 🕹":
        if secsudo(m):
            await restart(c, m)
        else:
            await m.reply_text("◍ انت لست المطور الاساسي\n√")
            return


########################################################################################################################
########################################################################################################################

    if m.text == "السورس" or m.text == "سورس" or m.text == "يا سورس":
        Marcelo = await c.get_users(super_sudoers[1])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(
                             Marcelo.first_name, user_id=super_sudoers[1]
            )
            ], 
            [ InlineKeyboardButton ( "CH SOURCE", url=f"https://t.me/Source_Theo" )], 
        [InlineKeyboardButton("اضف البوت الي مجموعتك ✅",
                              url=f"https://t.me/{get_bot_information () [1]}?startgroup=new")],
        ])
        await m.reply_text("""
╭──── • ◈ • ────╮
么 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗵𝗲𝗼](t.me/Source_Theo)
么 [𝗦𝗼𝘂𝗿𝗰𝗲 𝗕𝗼𝘁](t.me/R40_bot)
么 [𝗠𝗮𝗿𝗰𝗲𝗹𝗼](t.me/XIX_A)
╰──── • ◈ • ────╯

⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
        """, reply_markup=keyboard, parse_mode=enums.ParseMode.MARKDOWN)

    if m.text == "مطور" or m.text == "المطور" or m.text == "مطور البوت":
        s = await c.get_users(super_sudoers[1])
        n = await c.get_users(sudoers[0])
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(f"{s.first_name}", user_id=super_sudoers[1])],
            [InlineKeyboardButton(f"{n.first_name}", user_id=sudoers[0])],
            [InlineKeyboardButton("ضيـف البـوت لمجمـوعتـك ✅",
                                  url=f"https://t.me/{get_bot_information()[1]}?startgroup=new")],
        ])
        try:
            await c.get_chat_photos(sudoers[0], limit=1).__anext__()
        except:
            await m.reply_text("◍ الاول: هو مطور السورس \n◍ الثاني: هو صاحب البوت\n√", reply_markup=keyboard)
        else:
            async for photo in c.get_chat_photos(sudoers[0], limit=1):
                    await m.reply_photo(photo.file_id, caption="◍ الاول: هو مطور السورس \n◍ الثاني: هو صاحب البوت\n√", reply_markup=keyboard)
        return

    if m.text == "نور" or m.text == "نور":
        s = await c.get_users("6799500549")
        ss = (await c.get_chat("6799500549")).bio
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(f"{s.first_name}", user_id=6799500549)],
        ])
        try:
            await c.get_chat_photos("6799500549", limit=1).__anext__()
        except:
            await m.reply_text(f"{ss}", reply_markup=keyboard),
        else:
            async for photo in c.get_chat_photos("6367618993", limit=1):
                    await m.reply_photo(photo.file_id, caption=f"{ss}", reply_markup=keyboard),
        return

    if m.text == "تغيير المطور الاساسي" or m.text == "تغير المطور الاساسي":
        if sudo(m):
            set_db_wait("changesudo", m.from_user.id, m.chat.id)
            await m.reply_text("◍ ارسل لى ايدي المطور\n√")
            return
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "id" or m.text == "ايدي" or m.text == "ايدى" or m.text == "الايدي" or m.text == "الايدى" or m.text == "ايديه":
        await ids_private(c, m)
        return

    if m.text == "رتبتي" or m.text == "رتبتى":
        await m.reply_text("◍ رتبتك في البوت » " + await get_Rank(m))
        return


    if m.text == "بوت" or m.text == "البوت":
        if sudo2(m):
            await m.reply_text("◍ نعم حبيبى المطور 🥺❤️\n√")
        else:
            if manager(m):
                await m.reply_text("◍ نعم حبيبي المالك 🥺❤️\n√")
            else:
                if constractors(m):
                    await m.reply_text("◍ نعم حبيبى المنشئ 🥺❤️\n√")
                else:
                    if admin(m):
                        await m.reply_text("◍ نعم حبيبى الادمن 🥺❤️\n√")
                    else:
                        if special(m):
                            await m.reply_text("◍ نعم حبيبى المميز 🥺❤️\n√")
                        else:
                            if get_db_botname() is None:
                                botname = "ثيو"
                            else:
                                botname = get_db_botname()
                            await m.reply_text("اسمى " + botname + " ياحب 🙄❤️")

    if m.text == (get_db_botname() or "ثيو"):
        texting = ["اؤمر " + (get_db_botname() or "ثيو") + " شتريد؟❤️🥺",
                   "اى يقلب " + (get_db_botname() or "ثيو") + "❤️",
                   "موجود عايز اى بوشك ده😒",
                   "موجود عاوز اى 😒",
                   "مالك حبيبى🥺",
                   "شفلك كلبه❤️😂",
                   "مبكلمكش🥺",
                   "شبيك لبيك❤️😂",
                   "ثانيه واحده بتشقط وجى🙄",
                   "قلبى بينادى على " + (get_db_botname() or "ثيو1") + "😘",
                   "نعسان محدش يصحينى🙄"
                   ]
        await m.reply_text(random.choice(texting))
        return

    
    if m.text == "حساب العمر":
        await omrk(m)

    if m.text == "الاوامر" or m.text == "اوامر" or m.text == "م1" or m.text == "m1" or m.text == "م2" \
            or m.text == "m2" or m.text == "م3" or m.text == "m3" or m.text == "م4" or m.text == "m4" \
            or m.text == "م5" or m.text == "m5" or m.text == "m6" or m.text == "م6":
        await command(c, m)
        return

    if m.text == "قرءان" or m.text == "قران" or m.text == "قرآن" or m.text == "القرآن" or m.text == "القرءان":
        await quran(c, m)
        return

    if m.text == "استوري" or m.text == "ستوري":
        await status(c, m)
        return    
        
    if m.text == "رمزيات" or m.text == "رمزيه":
        await rmaziat(c, m)
        return

    if m.text == "غنيلي" or m.text == "غنيلى":
        await ghnely(c, m)
        return

    if m.text == "اغانى" or m.text == "اغاني":
        await music(c, m)
        return

    if m.text == "زخرفه" or m.text == "زخرفة" or m.text == "الزخرفه":
        await m.reply_text("◍ حسننا , الان يمكنك ارسال الاسم ليتم زخرفته بالعربى او بالنجليزى 🙄")
        set_db_wait("zhrfa", m.from_user.id, m.chat.id)
        return

    if m.text == "الافلام" or m.text == "افلام":
        await aflamAR(c, m)
        return

    if m.text == "كارتون" or m.text == "الكارتون" or m.text == "كرتون":
        await cartoon(c, m)
        return

    if m.text == "يوتيوب" or m.text == "اليوتيوب":
        if await lock_lockgenyoutube_test():
            await youtube_main(c, m)
            return
        else:
            await m.reply_text("◍ عذراا اليوتيوب فى الصيانه حاليا⚠️\n√")
            return

    if m.text == "انا فين":
        await m.reply_text(await get_Rank_ana_feen(m, c), parse_mode=enums.ParseMode.MARKDOWN)
        return

    if re.match("^قول (.*)$", str(m.text)):
        await echo_text(m)

    if re.match("^انطق (.*)$", str(m.text)):
        await say_text(m)


    if m.text == "بحبك" or m.text == "بحبك يابوت" or m.text == "يابوت بحبك":
        await m.reply_text(f"وانا كمان بعشقك يا [{m.from_user.first_name}](tg://user?id={m.from_user.id})💋🥰", parse_mode=enums.ParseMode.MARKDOWN)
                           
    if m.text == "رابط الحذف" or m.text == "رابط حذف" or m.text == "بوت حذف" or m.text == "بوت الحذف":
        texting = """
رابط الحذف في جميع مواقع التواصل ✸
فكر قبل لا تتسرع وتروح
ٴ≪━━━━━Theo━━━━━≫ٴ
◍ بوت حذف [Telegram](t.me/D62_bot) √
◍ رابط حذف [Telegram](https://my.telegram.org/auth?to=delete) √
◍ رابط حذف [instagram](https://www.instagram.com/accounts/login/?next=/accounts/remove/request/permanent/) √
◍ رابط حذف [Facebook](https://www.facebook.com/help/deleteaccount) √
◍ رابط حذف [Snspchat](https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fdeleteaccount) √
            """

        await m.reply_text(texting, parse_mode=enums.ParseMode.MARKDOWN)

        return

    if re.match("^طقس (.*)$", str(m.text)):
        await weather(c, m)
        return

    if m.text == "روايات" or m.text == "الروايات":
        await rwaiat(c, m)
        return

    if re.match("^معني (.*)$", str(m.text)) or re.match("^معنى (.*)$", str(m.text)):
        r = requests.get("https://leadermedo.herokuapp.com/name.php?leomedo=" + m.text[5:])
        rj = r.json()
        await m.reply_text(rj["meaning"])
        return

    if m.text == "الابراج" or m.text == "ابراج":
        await abrag(c, m)
        return

    if m.text == "تحويل" and m.reply_to_message:
        if m.reply_to_message.photo:
            await c.download_media(m.reply_to_message, file_name="./sticker.webp")
            await m.reply_sticker("sticker.webp")
            os.remove("sticker.webp")
            return
        if m.reply_to_message.sticker:
            await c.download_media(m.reply_to_message, file_name="./photo.jpg")
            await m.reply_photo("photo.jpg", caption=f"تم تحويل الملصق الى صوره بواسطه:\n @{get_bot_information()[1]}")
            os.remove("photo.jpg")
            return
        if m.reply_to_message.audio:
            await c.download_media(m.reply_to_message, file_name="./voice.ogg")
            await m.reply_voice("voice.ogg")
            os.remove("voice.ogg")
            return
        if m.reply_to_message.voice:
            await c.download_media(m.reply_to_message, file_name="./audio.mp3")
            await m.reply_audio("audio.mp3")
            os.remove("audio.mp3")
            return
        if m.reply_to_message.video:
            await c.download_media(m.reply_to_message, file_name="./animation.gif")
            await m.reply_animation("animation.gif")
            os.remove("animation.gif")
            return

    await games(c, m)
    await allreply_for_bot(c, m)


########################################################################################################################
########################################################################################################################

    if m.text == "حظر" and m.reply_to_message:
        if secsudo(m):
            await privbanrep(m)

    if re.match("^حظر @(.*)$", str(m.text)) or re.match("^حظر (\\d+)$", str(m.text)):
        if secsudo(m):
            await privbanuser(c, m)

    if m.text == "الغاء حظر" and m.reply_to_message:
        if secsudo(m):
            await privunbanrep(m)

    if re.match("^الغاء حظر @(.*)$", str(m.text)) or re.match("^الغاء حظر (\\d+)$", str(m.text)):
        if secsudo(m):
            await privunbanuser(c, m)

    if m.text == "المحظورين":
        if secsudo(m):
            lang = get_db_priban(m.chat.id)
            if lang is None:
                await m.reply_text("لا يوجد محظورين فى خاص البوت\n√")
            else:
                t = "\n◍ قائمه محظورين التواصل \n≪━━━━━━━━━━━━━≫\n"
                for row in lang:
                    t = t + f"[{row[1]}](tg://user?id={row[0]})\n"
                await m.reply_text(t, parse_mode=enums.ParseMode.MARKDOWN)
            return

    if m.text == "حذف المحظورين" or m.text == "مسح المحظورين":
        if secsudo(m):
            del_db_pribanall(m.chat.id)
            await m.reply_text("◍ تم حذف المحظورين\n√")
            return


########################################################################################################################
########################################################################################################################

    if m.text == "حذف داتابيز المحظورين":
        if sudo(m):
            del_db_banallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالمحظورين\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز المكتومين":
        if sudo(m):
            del_db_muteallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالمكتومين\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز مين ضافني":
        if sudo(m):
            del_db_meendafnyallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بمين ضافني\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز جهاتي":
        if sudo(m):
            del_db_mycontactallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالجهات\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز النقاط":
        if sudo(m):
            del_db_mypointgameallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالنقاط\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز رسائلي":
        if sudo(m):
            del_db_mymessageallall()
            await m.reply_text("◍ تم حذف الجدول الخاص برسائلي\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز ردود الجروب":
        if sudo(m):
            drop_db_replygroup()
            await m.reply_text("◍ تم حذف الجدول الخاص بردود الجروبات\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز قفل الدردشه":
        if sudo(m):
            drop_db_locktext()
            await m.reply_text("◍ تم حذف الجدول الخاص بالدردشه\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز الانتظار":
        if sudo(m):
            drop_db_wait()
            drop_db_waitq()
            await m.reply_text("◍ تم حذف الجدول الخاص بالانتظار\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return

    if m.text == "حذف داتابيز المحظورين خاص":
        if sudo(m):
            drop_db_pribanallall()
            await m.reply_text("◍ تم حذف الجدول الخاص بالمحظورين خاص\n√")
        else:
            await m.reply_text("◍ هذا الامر للمطور الاساسي فقط\n√")
            return


########################################################################################################################
########################################################################################################################

    if await lock_locksendmsg_test() and not sudo2(m):
        if m.text or m.photo or m.video or m.animation or m.audio or m.voice or m.document or m.contact or\
                m.reply_markup or m.game:
            await m.reply_text("◍ تم ارسال رسالتك الى المطور\n◍ سيتم الرد في اقرب وقت")
            await c.forward_messages(super_sudoers[0], m.from_user.id, m.id)
            await c.forward_messages(sudoers[0], m.from_user.id, m.id)

        if m.sticker:
            await m.reply_text("◍ تم ارسال رسالتك الى المطور\n◍ سيتم الرد في اقرب وقت")
            name = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
            await c.forward_messages(super_sudoers[0], m.from_user.id, m.id)
            await c.send_message(sudoers[1], "◍ تم ارسال الملصق من ↓\n - " + name, parse_mode=enums.ParseMode.MARKDOWN)
            await c.forward_messages(super_sudoers[0], m.from_user.id, m.id)
            await c.send_message(sudoers[0], "◍ تم ارسال الملصق من ↓\n - " + name, parse_mode=enums.ParseMode.MARKDOWN)

    if m.reply_to_message and secsudo(m) and m.text != "رفع نسخه احتياطيه":
        if m.text or m.photo or m.video or m.animation or m.audio or m.voice or m.document or m.contact or \
                m.reply_markup or m.game or m.sticker:
            try:
                name = f"[{m.reply_to_message.forward_from.first_name}]" \
                       f"(tg://user?id={m.reply_to_message.forward_from.id})"
                await c.forward_messages(m.reply_to_message.forward_from.id, m.chat.id, m.id)
                await m.reply_text(f"◍ تم ارسال رسالتك الى {name}", parse_mode=enums.ParseMode.MARKDOWN)
            except Exception as e:
                await m.reply_text(
                                   "", parse_mode=enums.ParseMode.MARKDOWN)
