from pyrogram import Client, filters
import requests
import yt_dlp
import asyncio
import yt_search  # Equivalent to yts-search in JS

YTMP4_API = "https://api.siputzx.my.id/api/d/ytmp4?url="

@Client.on_message(filters.command("song"))
async def song(client, message):
    query = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not query:
        await message.reply_text("Please provide a search query or YouTube URL.")
        return

    try:
        search_results = yt_search.YoutubeSearch(query, max_results=1).to_dict()
        if not search_results:
            await message.reply_text("No results found.")
            return
        
        video_url = f"https://www.youtube.com/watch?v={search_results[0]['id']}"
        title = search_results[0]['title']

        api_url = YTMP4_API + video_url
        response = requests.get(api_url)
        response.raise_for_status()  # Check if API request was successful
        data = response.json().get("data", {})

        if not data or 'dl' not in data:
            await message.reply_text("Failed to download the song.")
            return

        download_url = data['dl']
        
        await message.reply_text(f"Downloading {title}...")
        await client.send_audio(message.chat.id, audio=download_url, title=title, caption=title)

    except Exception as e:
        print(f"Error: {e}")
        await message.reply_text("An error occurred while processing your request. Please try again later.")
