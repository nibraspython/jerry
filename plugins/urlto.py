from pyrogram import Client, filters
import requests
import os

@Client.on_message(filters.command("url", "!") & filters.reply)
async def upload_to_catbox(client, message):
    if not message.reply_to_message or not message.reply_to_message.media:
        await message.reply("Reply to an image, video, or audio file.")
        return

    try:
        file_path = await message.reply_to_message.download()
        file_type = message.reply_to_message.document.mime_type if message.reply_to_message.document else None
        
        if "video" in file_type:
            filename = "upload.mp4"
            content_type = "video/mp4"
        elif "image" in file_type:
            filename = "upload.png"
            content_type = "image/png"
        elif "audio" in file_type:
            filename = "upload.mp3"
            content_type = "audio/mpeg"
        else:
            await message.reply("Unsupported file type.")
            os.remove(file_path)
            return

        with open(file_path, "rb") as file:
            response = requests.post("https://catbox.moe/user/api.php",
                                     files={"fileToUpload": (filename, file, content_type)},
                                     data={"reqtype": "fileupload"})
        
        os.remove(file_path)
        file_url = response.text.strip()
        await message.reply(file_url)
    
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
