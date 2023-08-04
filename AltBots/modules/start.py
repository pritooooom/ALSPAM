from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("💘 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚂 💘", data="help_back")
    ],
    [
        Button.url("🌺 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚁 🌺", "https://t.me/PRADHAN474"),
        Button.url("🌸 𝚂𝚞𝚙𝚙𝚘𝚛𝚃 🌸", "https://t.me/BWANDARLOK")
    ],
    [
        Button.url("💖 𝙾𝚡𝚢𝙶𝚎𝙽 💖", "https://t.me/PRADHAN474")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **𝙼𝚢 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁 : 🦋⃟ ᴠͥɪͣᴘͫ 🇴 🇽 𝐘 𝐆 𝐄 𝐍⃝⃝⃪⃕🥀**\n\n"
        TEXT += f"» **𝙱𝙾𝚃𝚂 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `M3.3`\n"
        TEXT += f"» **𝙿𝚈𝚃𝙷𝙸𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** `3.11.3`\n"
        TEXT += f"» **𝙾𝚇𝚈𝙶𝙴𝙽 ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/b0825ba6490d2aa6a6afd.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
