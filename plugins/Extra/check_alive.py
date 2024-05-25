import time
import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CMD = ["/", "."]

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

@Client.on_message(filters.command("Channels", CMD))
async def channels(_, message):
    keyboard = [
        [
            InlineKeyboardButton("🍁 ʜᴅ ᴛᴇʟᴜɢᴜ ᴍᴏᴠɪᴇs 🎖️", url="https://t.me/+wIa9vb3tRho3N2Q1")
        ],
        [
            InlineKeyboardButton("🧞‍♀️ ʜɪɴᴅɪ - ᴍᴀʟᴀʏᴀʟᴀᴍ 🧐", url="https://t.me/+97U9EyGMz_s2YzQ1"),
            InlineKeyboardButton("🔔 ᴛᴀᴍɪʟ - ᴋᴀɴɴᴀᴅᴀ 🤖", url="https://t.me/+a3-YTIF0zsFhMDc1")
        ],
        [
            InlineKeyboardButton("🔥 ʜᴏʟʟʏᴡᴏᴏᴅ - ᴅᴜʙʙᴇᴅ 🎉", url="https://t.me/+9Ks800pBuq9kMmNl"),
            InlineKeyboardButton("🙂 ᴡᴇʙ - sᴇʀɪᴇs ✨", url="https://t.me/+YcesJaZ8gwUyMTc1")
        ],
        [
            InlineKeyboardButton("🥵 ʀᴀʀᴇ ʜɪᴅᴅᴇɴ ᴍᴏᴠɪᴇꜱ ♥️", url="https://t.me/PIFRareHiddenMovies")
        ],
        [
            InlineKeyboardButton("☀️ ᴅᴠᴅ - ᴅᴀᴛᴀʙᴀsᴇ 🌚", url=""),
            InlineKeyboardButton("🌿 ʜᴅ - ᴅᴀᴛᴀʙᴀsᴇ 💧", url="")
        ],
        [
            InlineKeyboardButton("🔗 ʙᴏᴛᴢ ᴀʀᴇᴀ ⚙", url="https://t.me/BoTzUpdates0"),
            InlineKeyboardButton("🥵 ᴏɴʟʏ ᴀᴅᴜʟᴛꜱ 🙈", url="https://t.me/PIFOficial")
        ],
        [
            InlineKeyboardButton("⪦ ᴍᴏᴠɪᴇs ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ⪧", url="https://t.me/+37-TDCcQqltlOTRl")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text(
        text="""**🙃 __Welcome To My PanindiaFilmZ Community!! Cheak Our Channels & Groups List Below!!**__

__**He'llo 👋🏻 .. I Am  PanindiaFilmZ Admin, My Channels Invite links 👇🏻 ** __

__**🌟 #PANINDIAFILMZ #OURMENIA 3D~EXP🔥 **__

**__✨  Deals 24/7 :- 
@Killer_Loot_Deals __**

**__✨ Rare Hidden Adult Movies 2.0 
@Telugu_Adults_Rare_Hidden_Movies__**

__**ᴀʟʟ ʟᴀɴɢᴜᴀɢᴇ ɴᴇᴡ ᴍᴏᴠɪᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ | தமிழ் | తెలుగు | हिंदी | മലയാളം | ಕನ್ |**__

__**Target - Reaching ur Self 🎯**__

__**For Any Queries - @PIFAdminBot**__

__**@PanindiaFilmZ 🔥**__""",
        reply_markup=reply_markup
    )
