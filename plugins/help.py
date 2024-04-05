from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

HELPP_TEXT = """Yo, Komi here a telegram management bot written on pyrogram library 

Check the following buttons for more info 

Report bugs at - @komisan_support"""


@Client.on_message(filters.command('help') | filters.command('help@KomiSanRobot'))
def bothelp(_, message):
    if message.chat.type == "private":
        keyboard = []
        for x in help_message:
            keyboard.append([
                InlineKeyboardButton(f"{x['Module_Name']}",
                                     callback_data=f"help:{x['Module_Name']}")
            ])

        message.reply_text(
            HELPP_TEXT,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    else:
        message.reply_photo(
            photo="https://telegra.ph/file/769474503795f6d4f406c.jpg",
            caption=HELPP_TEXT,
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton(
                    "Pm me for more details",
                    url="t.me/komisanrobot?start=help")
            ]])
        )
