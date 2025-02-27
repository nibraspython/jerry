from pyrogram import Client, filters
import yt_dlp
import requests
import os

YTMP4_API = "https://api.siputzx.my.id/api/d/ytmp4?url="
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

def download_audio(video_url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
            'noplaylist': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            return info['title'], filename
    except Exception as e:
        print(f"Download Error: {e}")
        return None, None

@Client.on_message(filters.command("song"))
async def song(client, message):
    query = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply_text("Please provide a search query or YouTube URL.")
        return
    
    response = requests.get(f"https://www.youtube.com/results?search_query={query}")
    if 'watch?v=' not in response.text:
        await message.reply_text("No results found.")
        return
    
    video_url = f"https://www.youtube.com/watch?v={response.text.split('watch?v=')[1].split('"')[0]}"
    title, audio_path = download_audio(video_url)
    if not audio_path:
        await message.reply_text("Failed to download the audio.")
        return
    
    await message.reply_text(f"Uploading {title}...")
    await client.send_audio(message.chat.id, audio=audio_path, title=title)
    os.remove(audio_path)  # Delete after sending

@Client.on_message(filters.command("video"))
async def video(client, message):
    query = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply_text("Please provide a search query or YouTube URL.")
        return
    
    response = requests.get(YTMP4_API + query)
    data = response.json().get("data", {})
    if not data:
        await message.reply_text("Failed to download the video.")
        return
    
    await message.reply_text(f"Uploading {data['title']}...")
    await client.send_video(message.chat.id, video=data['dl'], caption=data['title'])
