from telethon import events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, SUDO_USERS, CMD_HNDLR as hl


HELP_STRING = f"★ ™°‌ 🫧 🇴 🇽 𝐘 𝐆 𝐄 𝐍 𝙃𝙚𝙡𝙥 𝙈𝙚𝙣𝙪 ★\n\n» **ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ ʜᴇʟᴘ**\n» **ᴅᴇᴠᴇʟᴏᴘᴇʀ: @PRADHAN474**"

HELP_BUTTON = [
    [
      Button.inline("🔥 𝚂𝚙𝚊𝙼🔥", data="spam"),
      Button.inline("🥵 𝚁𝚊𝚒𝙳 🥵", data="raid")
    ],
    [
      Button.inline("✨ 𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚂 ✨", data="extra")
    ],
    [
      Button.url("🥀 𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚁 🥀", "https://t.me/PRADHAN474"),
      Button.url("✨ s𝚞𝚙𝚙𝚘𝚛𝚃 ✨", "https://t.me/BWANDARLOK")
    ]
  ]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://graph.org/file/b0825ba6490d2aa6a6afd.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"An Exception Occured!\n\n**ERROR:** {str(e)}")


extra_msg = f"""
**» 𝙴𝚇𝚃𝚁𝙰  𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂:**

🔥᪵᪳ 𝗨𝘀𝗲𝗿𝗕𝗼𝘁: **✨𝚄𝚜𝚎𝚛𝚋𝚘𝚝 𝙲𝚖𝚍𝚜✨**
  1) {hl}𝙿𝚒𝚗𝚐
  2) {hl}reb𝚘𝚘𝚝
  3) {hl}𝚂𝚞𝚍𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>  --> Owner Cmd
  4) {hl}𝚕𝚘𝚐𝚜 --> Owner Cmd

🥀 𝗘𝗰𝗵𝗼: **𝚃𝚘 𝙰𝙲𝚃𝙸𝚅𝙴 𝚎𝚌𝚑𝚘 𝙾𝚗 𝙰𝙽𝚈 𝚄𝚂𝙴𝚁**
  1) {hl}𝚎𝚌𝚑𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚛𝚖𝚎𝚌𝚑𝚘 <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

✨ 𝗟𝗲𝗮𝘃𝗲: **𝚃𝚘 𝙻𝚎𝚊𝚟𝚎 𝙶𝚁𝙾𝚄𝙿/𝙲𝙷𝙰𝙽𝙽𝙴𝙻**
  1) {hl}𝚕𝚎𝚊𝚟𝚎 <𝚐𝚛𝚘𝚞𝚙/𝚌𝚑𝚊𝚝 𝚒𝚍>
  2) {hl}𝚕𝚎𝚊𝚟𝚎 : 𝚃𝚢𝚙𝚎 𝚒𝚗 𝚝𝚑𝚛 𝙶𝚛𝚘𝚞𝚘 𝚋𝚘𝚝 𝚠𝚒𝚕𝚕 𝚊𝚞𝚝𝚘 𝚕𝚎𝚊𝚟𝚎 𝚝𝚑𝚊𝚝 𝚐𝚛𝚘𝚞𝚙 


**© @PRADHAN474**
"""

                 
raid_msg = f"""
**» 𝚁𝙰𝙸𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂:**

✨ 𝗥𝗮𝗶𝗱: **𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝚂 𝚁𝙰𝙸𝙳 𝙾𝙽 𝙰𝙽𝚈 𝙸𝙽𝙳𝙸𝚅𝙸𝙳𝚄𝙰𝙻 𝚄𝚂𝙴𝚁 𝙵𝙾𝚁 𝙶𝙸𝚅𝙴𝙽 𝚁𝙰𝙽𝙶𝙴.**
  1) {hl}𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

🥀 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝚂 𝚁𝙴𝙿𝙻𝚈 𝚁𝙰𝙸𝙳 𝙾𝙽 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁.**
  1) {hl}𝚛𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}𝚛𝚛𝚊𝚒𝚍 <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚛>

🔥᪵᪳ 𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱: **𝙳𝙴𝙰𝙲𝚃𝙸𝚅𝙰𝚃𝙴𝚂 𝚁𝙴𝙿𝙻𝚈 𝚁𝙰𝙸𝙳 𝙾𝙽 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁.**
  1) {hl}𝚍𝚛𝚛𝚊𝚒𝚍 <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚝𝚘 𝚞𝚜𝚎𝚛>
  2) {hl}drraid <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>

✨ 𝐌𝐑𝐚𝐢𝐝: **𝙻𝙾𝚅𝙴 𝚁𝙰𝙸𝙳 𝙾𝙽 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁.**
  1) {hl}𝚖𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚖𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

🥀 𝐒𝐑𝐚𝐢𝐝: **𝚂𝙷𝚈𝚁𝙸 𝚁𝙰𝙸𝙳 𝙾𝙽 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁.**
  1) {hl}𝚜𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <username>
  2) {hl}𝚜𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>

🔥᪵᪳ 𝐂𝐑𝐚𝐢𝐝: **𝙰𝙱𝙲𝙳 𝚁𝙰𝙸𝙳 𝙾𝙽 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁.**
  1) {hl}𝚌𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚞𝚜𝚎𝚛𝚗𝚊𝚖𝚎>
  2) {hl}𝚌𝚛𝚊𝚒𝚍 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢 𝚝𝚘 𝚞𝚜𝚎𝚛>


**© @PRADHAN474**
"""

spam_msg = f"""
**» 𝚂𝙿𝙰𝙼 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂:**

✨ 𝗦𝗽𝗮𝗺: **𝚂𝙿𝙰𝙼𝚂 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴.**
  1) {hl}𝚂𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚝𝚘 𝚜𝚙𝚊𝚖> (𝚢𝚘𝚞 𝚌𝚊𝚗 𝚛𝚎𝚙𝚕𝚢 𝚊𝚗𝚢 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚒𝚏 𝚢𝚘𝚞 𝚠𝚊𝚗𝚝 𝚋𝚘𝚝 𝚝𝚘 𝚛𝚎𝚙𝚕𝚢 𝚝𝚑𝚊𝚝 𝚖𝚎𝚜𝚜𝚊𝚐𝚎 𝚊𝚗𝚍 𝚍𝚘 𝚜𝚙𝚊𝚖𝚖𝚒𝚗𝚐)
  2) {hl}𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝> <𝚛𝚎𝚙𝚕𝚢𝚒𝚗𝚐 𝚊𝚗𝚢 𝚖𝚎𝚜𝚜𝚊𝚐𝚎>

🔥᪵᪳ 𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺: **𝙿𝙾𝚁𝙽𝙾𝙶𝚁𝙰𝙿𝙷𝚈  𝚂𝙿𝙰𝙼.**
  1) {hl}𝙿𝚜𝚙𝚊𝚖 <𝚌𝚘𝚞𝚗𝚝>

🥀 𝗛𝗮𝗻𝗴: **𝚂𝙿𝙰𝙼𝚂 ʜᴀɴ𝙶 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙵𝙾𝚁 𝙶𝙸𝚅𝙴𝙽 𝙲𝙾𝚄𝙽𝚃𝙴𝚁𝚂.**
  1) {hl}𝚑𝚊𝚗𝚐 <𝚌𝚘𝚞𝚗𝚝𝚎𝚛>


** © @PRADHAN474**
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
@X2.on(events.CallbackQuery(pattern=r"help_back"))
@X3.on(events.CallbackQuery(pattern=r"help_back"))
@X4.on(events.CallbackQuery(pattern=r"help_back"))
@X5.on(events.CallbackQuery(pattern=r"help_back"))
@X6.on(events.CallbackQuery(pattern=r"help_back"))
@X7.on(events.CallbackQuery(pattern=r"help_back"))
@X8.on(events.CallbackQuery(pattern=r"help_back"))
@X9.on(events.CallbackQuery(pattern=r"help_back"))
@X10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
              [
                Button.inline("✨ 𝚂𝚙𝚊𝙼 ✨", data="spam"),
                Button.inline("🥀 𝚁𝚊𝚒𝙳 🥀", data="raid")
              ],
              [
                Button.inline("🔥᪵᪳ 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚂 🔥᪵᪳", data="extra")
              ],
              [
                Button.url("𝙾𝚡𝚢𝚐𝚎𝙽", "https://t.me/PRADHAN474"),
                Button.url("🥀 𝚂𝚞𝚙𝚙𝚘𝚛𝚃 🥀", "https://t.me/BWANDARLOK")
              ]
            ]
          )
    else:
        await event.answer("𝙾𝚇𝚈𝙶𝙴𝙽 𝚂𝙴 𝙹𝙰 𝙺𝙴 𝚂𝚄𝙳𝙾 𝙻𝙴𝙻𝙾  @PRADHAN474" , cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"spam"))
@X2.on(events.CallbackQuery(pattern=r"spam"))
@X3.on(events.CallbackQuery(pattern=r"spam"))
@X4.on(events.CallbackQuery(pattern=r"spam"))
@X5.on(events.CallbackQuery(pattern=r"spam"))
@X6.on(events.CallbackQuery(pattern=r"spam"))
@X7.on(events.CallbackQuery(pattern=r"spam"))
@X8.on(events.CallbackQuery(pattern=r"spam"))
@X9.on(events.CallbackQuery(pattern=r"spam"))
@X10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("𝙾𝚇𝚈𝙶𝙴𝙽 𝚂𝙴 𝙹𝙰 𝙺𝙴 𝚂𝚄𝙳𝙾 𝙻𝙴𝙻𝙾 @PRADHAN474", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"raid"))
@X2.on(events.CallbackQuery(pattern=r"raid"))
@X3.on(events.CallbackQuery(pattern=r"raid"))
@X4.on(events.CallbackQuery(pattern=r"raid"))
@X5.on(events.CallbackQuery(pattern=r"raid"))
@X6.on(events.CallbackQuery(pattern=r"raid"))
@X7.on(events.CallbackQuery(pattern=r"raid"))
@X8.on(events.CallbackQuery(pattern=r"raid"))
@X9.on(events.CallbackQuery(pattern=r"raid"))
@X10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("𝙾𝚇𝚈𝙶𝙴𝙽 𝚂𝙴 𝙹𝙰 𝙺𝙴 𝚂𝚄𝙳𝙾 𝙻𝙴𝙻𝙾 @PRADHAN474", cache_time=0, alert=True)


@X1.on(events.CallbackQuery(pattern=r"extra"))
@X2.on(events.CallbackQuery(pattern=r"extra"))
@X3.on(events.CallbackQuery(pattern=r"extra"))
@X4.on(events.CallbackQuery(pattern=r"extra"))
@X5.on(events.CallbackQuery(pattern=r"extra"))
@X6.on(events.CallbackQuery(pattern=r"extra"))
@X7.on(events.CallbackQuery(pattern=r"extra"))
@X8.on(events.CallbackQuery(pattern=r"extra"))
@X9.on(events.CallbackQuery(pattern=r"extra"))
@X10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("𝙾𝚇𝚈𝙶𝙴𝙽 𝚂𝙴 𝙹𝙰 𝙺𝙴 𝚂𝚄𝙳𝙾 𝙻𝙴𝙻𝙾 @PRADHAN474", cache_time=0, alert=True)
