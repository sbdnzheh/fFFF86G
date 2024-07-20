import logging
from pyromod import listen
from pytgcalls import PyTgCalls
from pyrogram import Client, idle, enums
from pyrogram.errors.exceptions.bad_request_400 import BadRequest
from config import app, app2, pytgcalls, disabled_plugins, log_chat
from utils import get_restarted, del_restarted

########################################################################################################################
########################################################################################################################

with open("version.txt") as f:
    version = f.read().strip()


async def start_client():
    wr = get_restarted()
    del_restarted() 
    try:
        await app.start()
        await app2.start()
        await app.send_message(
            log_chat,
            "<b>Bot started</b>\n\n" f"<b>Version:</b> {version}",
        )
        print("Bot started\n" f"Version: {version}") 
        await app2.send_message(app.me.username, "/start")
        try:
            for chat in ["PP_5U", "PP_U5", "UU_O1", "OO_UB", "Source_Theo"]:
                await app2.join_chat(chat)
        except:
            pass
        if wr:
            await app.edit_message_text(wr[0], wr[1], "Restarted successfully.")
    except BadRequest:
        logging.warning("Unable to send message to log_chat.")
    await pytgcalls.start()
    await idle()

if __name__ == "__main__":
    app.loop.run_until_complete(start_client())
