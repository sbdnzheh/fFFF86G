import asyncio
import html
import io
import os
import re
import sys
import traceback
from contextlib import redirect_stdout
import speedtest
from meval import meval
from pyrogram import Client, filters, enums
from pyrogram.types import Message
from pyrogram.errors import RPCError
from config import prefix, sudoers
from utils import set_restarted


async def upgrade(c: Client, m: Message):
    sm = await m.reply_text("◍ جارى التحديث...")
    proc = await asyncio.create_subprocess_shell("git pull --no-edit",
                                                 stdout=asyncio.subprocess.PIPE,
                                                 stderr=asyncio.subprocess.STDOUT)
    stdout = (await proc.communicate())[0]
    if proc.returncode == 0:
        if "◍ بالفعل انت على اخر تحديث\n√" in stdout.decode():
            await sm.edit_text("◍ لايوجد اى تحديثات جديده\n√")
        else:
            await sm.edit_text("إعادة التشغيل...")
            set_restarted(sm.chat.id, sm.id)
            os.execl(sys.executable, sys.executable, *sys.argv)  # skipcq: BAN-B606
    else:
        await sm.edit_text(f"◍ فشل التحديث (process exited with {proc.returncode}):\n{stdout.decode()}")
        proc = await asyncio.create_subprocess_shell("git merge --abort")
        await proc.communicate()


@Client.on_message(filters.command("eval", prefix) & filters.user(sudoers))
async def evals(c: Client, m: Message):
    text = m.text.split(maxsplit=1)[1]
    try:
        res = await meval(text, globals(), **locals())
    except:  # skipcq
        ev = traceback.format_exc()
        await m.reply_text(f"<code>{html.escape(ev)}</code>")
    else:
        try:
            await m.reply_text(f"<code>{html.escape(str(res))}</code>")
        except Exception as e:  # skipcq
            await m.reply_text(str(e))


@Client.on_message(filters.command("exec", prefix) & filters.user(sudoers))
async def execs(c: Client, m: Message):
    strio = io.StringIO()
    code = m.text.split(maxsplit=1)[1]
    exec("async def __ex(c, m): " + " ".join("\n " + l for l in code.split("\n")))  # skipcq: PYL-W0122
    with redirect_stdout(strio):
        try:
            await locals()["__ex"](c, m)
        except:  # skipcq
            return await m.reply_text(html.escape(traceback.format_exc()))

    if strio.getvalue().strip():
        out = f"<code>{html.escape(strio.getvalue())}</code>"
    else:
        out = "Command executed."
    await m.reply_text(out)


async def test_speed(c: Client, m: Message):
    sent = await m.reply_text(f"**سرعه**\n\n**🌐 المضيف:**\n\n**🏓 بينج: م.م.م.**\n**⬇️ تنزيل: ميجابايت**\n**⬆️ رفع: ميجابايت**", parse_mode=enums.ParseMode.MARKDOWN)
    s = speedtest.Speedtest()
    bs = s.get_best_server()
    await sent.edit_text(f"**سرعه**\n\n**🌐 المضيف:** {bs['sponsor']}\n\n**🏓 بينج:** {int(bs['latency'])} م.م.م.\n**⬇️ تنزيل:** ميجابايت\n**⬆️ رفع:** ميجابايت", parse_mode=enums.ParseMode.MARKDOWN)
    dl = round(s.download() / 1024 / 1024, 2)
    await sent.edit_text(f"**سرعه**\n\n**🌐 المضيف:** {bs['sponsor']}\n\n**🏓 بينج:** {int(bs['latency'])} م.م.م.\n**⬇️ تنزيل:** {dl} ميجابايت\n**⬆️ رفع:** ميجابايت", parse_mode=enums.ParseMode.MARKDOWN)
    ul = round(s.upload() / 1024 / 1024, 2)
    await sent.edit_text(f"**سرعه**\n\n**🌐 المضيف:** {bs['sponsor']}\n\n**🏓 بينج:** {int(bs['latency'])} م.م.م.\n**⬇️ تنزيل:** {dl} ميجابايت\n**⬆️ رفع:** {ul} ميجابايت", parse_mode=enums.ParseMode.MARKDOWN)


async def restart(c: Client, m: Message):
    sent = await m.reply_text("إعادة التشغيل...")
    os.execl(sys.executable, sys.executable, *sys.argv)  # skipcq: BAN-B606


async def del_message(c: Client, m: Message):
    try:
        await c.delete_messages(
            m.chat.id,
            m.reply_to_message.id
        )
    except Exception as e:
        print("del message" + str(e))
    try:
        await c.delete_messages(
            m.chat.id,
            m.id
        )
    except RPCError as e:
        print("del message" + str(e))
