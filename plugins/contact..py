#CREATED BY @TheRiZoeL
#PROVIDED BY @NovaXMod



#IMPORTS
from pyrogram import filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from name import pbot as Client

#VARS
support_chat_id =
devs = []

#CLIENT
@Client.on_message(filters.private & filters.command(['cont', 'req', 'contact']))
async def contact(RiZoeL, message):
   await message.reply('Click below button to contact devs!', reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Contact↗️", callback_data="contact")]]))

@Client.on_message(filters.chat(support_chat_id) & filters.user(devs) & filters.text)
async def devs_reply(RiZoeL, message):
  re = message.reply_to_message
  if re.forward_from:
     await RiZoel.send_message(
       re.forward_from.id,
       message.text.markdown,
       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Contact Again ↗️", callback_data="contact")]]),
     )
   
@Client.on_callback_query()
async def cont_callbacks(RiZoeL: Client, callback_query: CallbackQuery):
   if callback_query.data.lower() == "contact":
      await callback_query.message.delete()
      conctact_message = await RiZoeL.ask(callback_query.message.chat.id, "How can I help? please send a message! \n\n**Lang:** Hindi | English", filters.text)
      await conctact_message.forward(support_chat_id)