import sys
import heroku3

from config import (
    X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID,
    SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl
)

from os import execl, getenv
from telethon import events
from datetime import datetime

connected_chats = [X1, X2, X3, X4, X5, X6, X7, X8, X9, X10]

# Command decorator
def custom_command(pattern, **kwargs):
    def decorator(func):
        for chat in connected_chats:
            chat.on(events.NewMessage(incoming=True, pattern=pattern % hl, **kwargs)(func))
        return func
    return decorator

@custom_command(r"\%sping(?: |$)(.*)")
async def ping(event):
    if event.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await event.reply(f"» __™°‌ 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍__")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"💫🥀 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍\n» `{mp} 𝙼𝚂`")

@custom_command(r"\%sreboot(?: |$)(.*)")
async def restart(event):
    if event.sender_id in SUDO_USERS:
        await event.reply(f"`🥀𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝙱𝙾𝚃𝚂🥀...`")
        for chat in connected_chats:
            try:
                await chat.disconnect()
            except Exception:
                pass
        execl(sys.executable, sys.executable, *sys.argv)

@custom_command(r"\%ssudo(?: |$)(.*)")
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» __𝙰𝙳𝙳𝙸𝙽𝙶 𝚄𝚂𝙴𝚁 𝙰𝚂 💘𝚂𝚄𝙳𝙾💘...__🚀🚀")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("`[HEROKU]:" "\nPlease Setup Your` **HEROKU_APP_NAME**")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» 🌺𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁🌺 !!")
            return

        if str(target) in sudousers:
            await ok.edit(f"🌸𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙰 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁🌸 !!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» **𝙽𝙴𝚆 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 ™°‌**: `{target}`\n» `𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 `💖𝙱𝙾𝚃𝚂💖")
            heroku_var["SUDO_USERS"] = newsudo

@custom_command(r"\%ssudolist(?: |$)(.*)")
async def list_sudo_users(event):
    if event.sender_id in SUDO_USERS:
        sudo_list_text = "\n".join(f"- `{user_id}`" for user_id in SUDO_USERS)
        await event.reply(f"List of sudo users:\n{sudo_list_text}")

@custom_command(r"\%sbroadcast(?: |$)(.*)")
async def broadcast(event):
    if event.sender_id in SUDO_USERS:
        message = event.pattern_match.group(1)
        for chat in connected_chats:
            await chat.send_message(message)
        await event.reply("Broadcast sent to all connected chats.")

@custom_command(r"\%sgban(?: |$)(.*)")
async def gban_user(event):
    if event.sender_id in SUDO_USERS:
        user_id = event.pattern_match.group(1)
        globally_banned_users.add(user_id)
        await event.reply(f"User with ID {user_id} has been globally banned.")

# ... Your other functions ...

# Main loop
if __name__ == "__main__":
    for chat in connected_chats:
        chat.run_until_disconnected()
