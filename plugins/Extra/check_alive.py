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
            InlineKeyboardButton("🍁 ᴛᴀᴍɪʟ - ᴋᴀɴɴᴀᴅᴀ 🎖️", url="https://t.me/+mGplIsWLBsNmMzdl")
        ],
        [
            InlineKeyboardButton("🧞‍♀️ ʜɪɴᴅɪ - ᴍᴀʟᴀʏᴀʟᴀᴍ 🧐", url="https://t.me/+Oc2rrg_Kl0hiN2Jl"),
            InlineKeyboardButton("🔔 ᴘᴀɴɪɴᴅɪᴀꜰɪʟᴍᴢ 🤖", url="https://t.me/PanindiaFilmZ")
        ],
        [
            InlineKeyboardButton("🛒 ᴅᴇᴀʟꜱ 🦾", url="https://t.me/Great_Indian_Shopping_loot_deals"),
            InlineKeyboardButton("🥵 ʀᴀʀᴇ ʜɪᴅᴅᴇɴ ᴍᴏᴠɪᴇꜱ ♥️", url="https://t.me/PIFRareHiddenMovies")
        ],
        [
            InlineKeyboardButton("🔗 ʙᴏᴛᴢ ᴀʀᴇᴀ", url="https://t.me/BoTzUpdates0"),
            InlineKeyboardButton("⚙ ᴍᴏᴠɪᴇꜱ ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/PIFOficial")
        ],
        [
            InlineKeyboardButton("⪦ ᴍᴏᴠɪᴇs ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ⪧", url="https://t.me/+37-TDCcQqltlOTRl")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await message.reply_text(
        text="""**🙃 __Welcome To My PanindiaFilmZ Community!! Cheak Our Channels & Groups List Below!!**__

__**Hi.. PanindiaFilmZ Admin, I Can Provide My Channels Invite links** __

__**🌟 #PANINDIAFILMZ #OURMENIA 3D~EXP🔥 **__

**__✨  GIS Deals 24/7 :- 
@Great_Indian_Shopping_loot_deals__**

**__✨ Rare Hidden Adult Movies 2.0 
@Telugu_Adults_Rare_Hidden_Movies__**

**__✨ PIF Fitter Bot :-
 @PanindiaFilmz_bot__**

**__✨ BoTz Updates :-
 @BoTzUpdates0__**

**__✨ File's Added Updates :- 
 @PIFOficials & @PIFOficial __**

__**ᴀʟʟ ʟᴀɴɢᴜᴀɢᴇ ɴᴇᴡ ᴍᴏᴠɪᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ | தமிழ் | తెలుగు | हिंदी | മലയാളം | ಕನ್ |**__

__**Target - Reaching ur Self 🎯**__

__**For Any Queries - @PanIndia_Flimz_Admin_bot**__

__**@PanindiaFilmZ 🔥**__""",
        reply_markup=reply_markup
                                )
