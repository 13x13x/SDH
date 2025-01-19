import time
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import instaloader
from datetime import datetime
from asyncio import Semaphore

CMD = ["/", "."]
loader = instaloader.Instaloader()
CONCURRENT_DOWNLOADS = 100
semaphore = Semaphore(CONCURRENT_DOWNLOADS)

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("**You are very lucky 🤞 I am alive ❤️ Press /start to use me**")

@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@Client.on_message(filters.command("IG", CMD) & filters.text)
async def ig_link_handler(client, message):
    if message.text.startswith(tuple(CMD)):
        return
    
    url = message.text.split(" ", 1)[-1].strip()  # Extract URL after "/IG"
    if not url:
        await message.reply_text("Please provide a valid Instagram URL after the command.")
        return
    
    chat_id = message.chat.id
    loading_message = await message.reply_text("⚡")

    try:
        # Extract shortcode from the URL
        url_parts = url.split("/")
        shortcode = url_parts[-2] if len(url_parts) > 2 else None
        
        if not shortcode:
            await loading_message.delete()
            await message.reply_text("Invalid Instagram URL provided.")
            return
        
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        media_urls = []
        captions = post.caption or " "

        if post.typename == "GraphSidecar":
            for edge in post.get_sidecar_nodes():
                media_urls.append(edge.video_url if edge.is_video else edge.display_url)
        else:
            media_urls.append(post.video_url if post.is_video else post.url)

        for i, media_url in enumerate(media_urls):
            file_name = f"{shortcode}_media_{i+1}" + (".mp4" if post.is_video else ".jpg")
            await client.send_document(
                chat_id,
                media_url,
                file_name=file_name,
                caption=f"**{captions}**\n\n**More Updates: @PanIndiaFilmZ**"
            )

        await loading_message.delete()
        
    except Exception as e:
        await loading_message.delete()
        print(f"Error: {e}")  # Debugging output
        await message.reply_text("**Try Again Later**")
