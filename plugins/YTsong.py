from pyrogram import Client, filters
import requests
import yt_dlp
import asyncio

YTMP4_API = "https://api.siputzx.my.id/api/d/ytmp4?url="

def download_audio(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        return info['title'], ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')

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
    
    video_id = response.text.split('watch?v=')[1].split('"')[0]  # Fixed syntax error
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    
    title, audio_path = download_audio(video_url)
    
    await message.reply_text(f"Downloading {title}...")
    await client.send_audio(message.chat.id, audio=audio_path, title=title)

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
    
    await message.reply_text(f"Downloading {data['title']}...")
    await client.send_video(message.chat.id, video=data['dl'], caption=data['title'])

@Client.on_message(filters.command("yta"))
async def yta(client, message):
    query = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply_text("Please provide a YouTube URL.")
        return
    
    title, audio_path = download_audio(query)
    await message.reply_text(f"Downloading {title}...")
    await client.send_audio(message.chat.id, audio=audio_path, title=title)

@Client.on_message(filters.command("ytv"))
async def ytv(client, message):
    query = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply_text("Please provide a YouTube URL.")
        return
    
    response = requests.get(YTMP4_API + query)
    data = response.json().get("data", {})
    if not data:
        await message.reply_text("Failed to download the video.")
        return
    
    await message.reply_text(f"Downloading {data['title']}...")
    await client.send_video(message.chat.id, video=data['dl'], caption=data['title'])

@Client.on_message(filters.command("jook"))
async def yts(client, message):
    query = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply_text("Please provide a search query.")
        return
    
    response = requests.get(f"https://www.youtube.com/results?search_query={query}")
    if 'watch?v=' not in response.text:
        await message.reply_text("No results found.")
        return
    
    results = [f"https://www.youtube.com/watch?v={vid.split('\"')[0]}" for vid in response.text.split('watch?v=')[1:10]]
    search_results = "\n".join([f"{i+1}. {vid}" for i, vid in enumerate(results)])
    await message.reply_text(f"Top 10 YouTube search results:\n\n{search_results}")
