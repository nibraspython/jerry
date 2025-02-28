from Script import script
from pyrogram.types import *
from pyrogram import Client, filters, enums
from info import PICS, LOG_CHANNEL, MSG_ALRT, DATABASE_URI, DATABASE_NAME
import os, random, asyncio
import time
import pymongo
from utils import temp

#hii 

inclient = pymongo.MongoClient(DATABASE_URI)
indb = inclient[DATABASE_NAME]
users = indb.users
group = indb.group

A = """{} with user id:- {} used /saavn command."""
B = """{} with user id:- {} used /vsaavn command."""

CMD = ["/", "."]

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...........")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"𝖯𝗂𝗇𝗀!\n{time_taken_s:.3f} ms")
    
CARBON_TXT = """**Hai {}, Here You Can Generate Carbon Image. Just Reply a Name /carbon**"""

SHARE_TXT = """**Hai {}, Here You Can Generate ShareText. Just Reply a Name /share**"""

START_MESSAGE = """
𝐇𝐞𝐥𝐥𝐨 <a href='tg://settings'>𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮⚡️</a>

𝐑𝐮𝐥𝐞𝐬 𝐀𝐧𝐝 𝐁𝐨𝐭 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 <a href='http://telegra.ph/Minnal-murali-03-06-12'>𝐂𝐥𝐢𝐜𝐤⚡️</a>


𝐅𝐨𝐫 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :-
/ssong 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐬𝐚𝐚𝐯𝐧 𝐦𝐩𝟑 𝐬𝐨𝐧𝐠
/svideo 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐬𝐚𝐚𝐯𝐧 𝐦𝐩𝟒 𝐬𝐨𝐧𝐠
/ysong 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐦𝐩𝟑 𝐬𝐨𝐧𝐠
/yvideo 𝐀𝐥𝐨𝐧𝐞✔️ =-= 𝐲𝐨𝐮𝐭𝐮𝐛𝐞 𝐦𝐩𝟒 𝐬𝐨𝐧𝐠
/Carbon
/paste
/carbon
/share
/json
/repo

/𝐬𝐚𝐚𝐯𝐧 𝐀𝐥𝐨𝐧𝐞 𝐄𝐧𝐠𝐥𝐢𝐬𝐡 ❌️
/𝐯𝐦𝐩𝟒 𝐀𝐥𝐨𝐧𝐞 𝐔𝐧𝐝𝐨❌️
/𝐲𝐬𝐨𝐧𝐠 𝐀𝐥𝐨𝐧𝐞 𝐒𝐨𝐧𝐠❌️
/𝐲𝐯𝐢𝐝𝐞𝐨 𝐀𝐥𝐨𝐧𝐞 𝐍𝐞𝐰❌️

𝐌𝐝𝐢𝐬𝐤 𝐋𝐢𝐧𝐤 𝐂𝐨𝐧𝐯𝐞𝐫𝐭𝐞𝐫
𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐀𝐧𝐝 𝐓𝐲𝐩𝐞 /stats 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐖𝐢𝐭𝐡 𝐘𝐨𝐮𝐫 𝐌𝐝𝐢𝐬𝐤 𝐋𝐢𝐧𝐤
𝐎𝐰𝐧𝐞𝐫 𝐍𝐚𝐦𝐞 :- {}
𝐆𝐫𝐨𝐮𝐩 𝐍𝐚𝐦𝐞 :- {}
"""

TEXT_TXT = """<b> Hᴇʟʟᴏ {}.

Mʏ Nᴀᴍᴇ Is {}.

I Cᴀɴ Pʀᴏᴠɪᴅᴇ Mᴏᴠɪᴇ Fᴏʀ Yᴏᴜ Jᴜsᴛ Aᴅᴅ Mᴇ Iɴ Yᴏᴜʀ Gʀᴏᴜᴘ Oʀ Jᴏɪɴ Oᴜʀ Gʀᴏᴜᴘ 🫶🏻🤍</b>"""

TEXT = """**Hai {},
I Am Password Generator Bot. I Can Generate Strong Passwords At Your Wish Length (Max. 84).**
For Know More /help"""

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🥤 Channel", url = "https://t.me/LEXUSOTP"),
            InlineKeyboardButton("Support Group 🥤", url = "https://t.me/NibrasHacked")
        ],
        [
            InlineKeyboardButton("🧃 Repo", url = "https://t.me/herokuaccountBot"),
            InlineKeyboardButton("Deploy 🧃", url = "https://t.me/ajzalup")
        ],
        [
            InlineKeyboardButton("📍 Developer 📍", url = "https://t.me/xax_ha_ha_l")
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


@Client.on_message(filters.command("start", CMD))
async def start(_, message):
    user = message.from_user.first_name
    user_id = message.from_user.id
    mention = message.from_user.mention
    buttons = [[
       InlineKeyboardButton('⛦ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ⛦', url=f'http://t.me/manikanddanbot?startgroup=true')
       ],[
       InlineKeyboardButton('⚙️ ꜰᴜɴᴛɪᴏɴ s⚙️', callback_data="jack"),
       InlineKeyboardButton('🧭 ᴀʙᴏᴜᴛ 🧭', callback_data="stick")
       ],[
       InlineKeyboardButton('🕸️ Hᴇʟᴩ', callback_data="file")
       ]]
    m = await message.reply_sticker("CAACAgIAAxkBAAIve2XgRl5w5qGTeAjktaUi00daPTyLAAIGMAACER1xSFRMh-rQSCkpNAQ") 
    await asyncio.sleep(2)
    await message.reply_photo(photo=random.choice(PICS), caption=script.ABOUT_TXT.format(message.from_user.mention, temp.B_NAME), reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    return await m.delete()
    await query.answer(MSG_ALRT)
    progress_document = users.find_one({"_id": user_id})
    if progress_document: 
        return
    else:
        users.update_one(
            {"_id": user_id},
            {"$set": {"name": user}},
            upsert=True
        )
        await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"<b>#NEW_USER\n\nNᴀᴍᴇ : {user}\nID : {user_id}</b>"
        )
        
@Client.on_message(filters.command("opin"))
async def pin(_, message: Message):
    if not message.reply_to_message: return
    await message.reply_to_message.pin()

@Client.on_message(filters.command("stats", CMD))
async def stats(client, message):
    from info import db  # Ensure db is imported properly

    try:
        users = db["users"]  # Access the users collection
        user_count = users.count_documents({})  # Count total users
        await message.reply_text(f"Total Users: {user_count}")
    except Exception as e:
        await message.reply_text(f"Error: {e}")  # Send error message to user

    
@Client.on_message(filters.new_chat_members & filters.me)
async def new_group(bot, message):
    name = message.chat.title
    group_id = message.chat.id
    progress_document = group.find_one({"_id": group_id})
    if progress_document: 
        return
    else:
        group.update_one(
            {"_id": group_id},
            {"$set": {"name": name}},
            upsert=True
        )
        await bot.send_message(
        chat_id=LOG_CHANNEL,
        text=f"<b>#NEW_GROUP\n\nNᴀᴍᴇ : {name}\nID : {group_id}</b>"
        )

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data == "file":
         buttons = [[
            InlineKeyboardButton(text="Carbon", callback_data="carb"),
            InlineKeyboardButton(text="Share", callback_data="shar"),
            ],[
            InlineKeyboardButton(text="About", callback_data="nibras"),
            ],[
            InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='start')
            ]]
         await query.message.edit_text("**Select Required Mode**", reply_markup=InlineKeyboardMarkup(buttons))
           
    elif query.data == "stick":
           buttons = [[
            InlineKeyboardButton(text="SongAi", callback_data="msong"),
            InlineKeyboardButton(text="Paste", callback_data="cur_ved"),
            ],[                    
            InlineKeyboardButton(text="Json", callback_data="help")
            ],[
            InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='start')
            ]]              
           await query.message.editt(text=script.NIBRAS_TXT, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(buttons), quote=True)
    if query.data == "start":
         buttons = [[
                    InlineKeyboardButton('⛦ 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 ⛦', url=f'http://t.me/oggyRbot?startgroup=true')
                ],[
                    InlineKeyboardButton('⚙️ ꜰᴜɴᴛɪᴏɴ y⚙️', callback_data="jack"),
                    InlineKeyboardButton('🧭 ᴀʙᴏᴜᴛ 🧭', callback_data="stick")
                ],[
                    InlineKeyboardButton('🕸️ Hᴇʟᴩ', callback_data="file")
                  ]]
         await query.message.edit_text(text=script.ABOUT_TXT, parse_mode=enums.ParseMode.HTML, reply_markup=InlineKeyboardMarkup(buttons))
    elif query.data == "jack":
           buttons = [[
            InlineKeyboardButton(text="ꜰᴜɴ", callback_data="stats"),
            InlineKeyboardButton(text="ᴩɪɴ", callback_data="cur_ved"),
            InlineKeyboardButton('ʀᴇᴩᴏʀᴛ', callback_data='start'),
            InlineKeyboardButton('ᴩᴜʀɢᴇ', callback_data='start')
            ],[
            InlineKeyboardButton(text="ᴀɪ 🤦🏼‍♂️", callback_data="ping"),
            InlineKeyboardButton(text="ᴛᴛꜱ", callback_data="cur_ved"),
            InlineKeyboardButton('ʙᴀɴ', callback_data='start'),
            InlineKeyboardButton(text="ᴇxᴛʀᴀ ᴍᴏᴅꜱ", callback_data="help")
            ],[
            InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='start')
            ]]              
           await query.message.edit(text=script.HELP_TXT, reply_markup=InlineKeyboardMarkup(buttons), parse_mode=enums.ParseMode.HTML)
    elif query.data == "msong":
           buttons = [[
           InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='file'), 
           InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'https://t.me/nibrashacked')
           ]]
           reply_markup = InlineKeyboardMarkup(buttons)
           await query.message.edit(text=START_MESSAGE, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
    elif query.data == "shar":
           buttons = [[
           InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='file'), 
           InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'https://t.me/nibrashacked')
           ]]
           reply_markup = InlineKeyboardMarkup(buttons)
           await query.message.edit(text=SHARE_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
    elif query.data == "carb":
           buttons = [[
           InlineKeyboardButton('𝙱𝙰𝙲𝙺', callback_data='file'), 
           InlineKeyboardButton('𝐉𝐨𝐢𝐧 𝐆𝐫𝐨𝐮𝐩', url=f'https://t.me/nibrashacked')
           ]]
           reply_markup = InlineKeyboardMarkup(buttons)
           await query.message.edit(text=CARBON_TXT, reply_markup=reply_markup, parse_mode=enums.ParseMode.HTML)
