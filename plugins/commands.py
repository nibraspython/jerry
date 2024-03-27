from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client, filters, enums
from info import PICS
import os, random, asyncio

CMD = ["/", "."]

@Client.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_photo(photo=random.choice(PICS), caption=ABOUT, reply_markup=InlineKeyboardMarkup(BUTTONS), parse_mode=enums.ParseMode.HTML)

TEXT = """**Hai {},
I Am Password Generator Bot. I Can Generate Strong Passwords At Your Wish Length (Max. 84).**
For Know More /help"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Channel 🔰", url = "https://telegram.me/EKBOTZ_UPDATE"),
            InlineKeyboardButton("Support Group ⭕️", url = "https://telegram.me/ekbotz_support")
        ],
        [
            InlineKeyboardButton("Repo 🗂️", url = "https://github.com/M-fazin/Password-Generator-Bot"),
            InlineKeyboardButton("Deploy 🗃️", url = "https://heroku.com/deploy?template=https://github.com/M-fazin/Password-Generator-Bot")
        ],
        [
            InlineKeyboardButton("Developer 💡", url = "https://github.com/M-fazin/")
        ]
    ]
)

HELP = """Hai {},
**There Is Nothing To Know More.**
- Send Me The Limit Of Your Password and Keys (optional)
  Like :-
    `10 abcd1234`
    `10`
- I Will Give The Password Of That Limit.
**Note :-**
• Only Digits Are Allowed
• Maximum Allowed Digits Till 100 (I Can't Generate Passwords Above The Length 84)"""

HELP_BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),
            InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Password-Generator-Bot")
        ]
    ]
)

ABOUT = """--**About Me**--
**🤖 Bot :** Password Generator Bot
**🧑‍💻 Developer :** [M-fazin](https://github.com/M-fazin)
**💻 Channel :** @EKBOTZ_UPDATE
**☎️ Support :** @ekbotz_support
**🗂️ Source Code :** [Password Generator Bot](https://github.com/M-fazin/Password-Generator-Bot)
**⚙️ Language :** Python 3
**🛡️ Framework :** Pyrogram"""


@Client.on_message(filters.command("help", CMD))
async def help(_, message):
        buttons = [[
                    InlineKeyboardButton('⛦ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ⛦', url=f'http://t.me/oggyRbot?startgroup=true')
                ],[
                    InlineKeyboardButton('🌐 Aʙᴏᴜᴛ', callback_data="about"),
                    InlineKeyboardButton('⚙️ Dᴏɴᴀᴛᴇ', url='https://t.me/xax_ha_ha_l')
                ],[
                    InlineKeyboardButton('🕸️ Hᴇʟᴩ', callback_data="help")
                  ]]
        m = await message.reply_sticker("CAACAgIAAxkBAAIve2XgRl5w5qGTeAjktaUi00daPTyLAAIGMAACER1xSFRMh-rQSCkpNAQ") 
        await asyncio.sleep(2)
        await message.reply_photo(photo=random.choice(PICS), caption=HELP, reply_markup=InlineKeyboardMarkup(buttons), parse_mode=enums.ParseMode.HTML)
        return await m.delete()
