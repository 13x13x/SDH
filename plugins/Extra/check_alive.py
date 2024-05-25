import time
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message, import InlineKeyboardMarkup, InlineKeyboardButton

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

@Client.on_message(filters.command("PIFchannels"))
async def PIFchannels(_, message: Message):

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
            InlineKeyboardButton("☀️ ᴅᴠᴅ - ᴅᴀᴛᴀʙᴀsᴇ 🌚", url="https://t.me/PIFOficials"),
            InlineKeyboardButton("🌿 ʜᴅ - ᴅᴀᴛᴀʙᴀsᴇ 💧", url="https://t.me/PIFOficial")
        ],
        [
            InlineKeyboardButton("🔗 ʙᴏᴛᴢ ᴀʀᴇᴀ ⚙", url="https://t.me/BoTzUpdates0"),
            InlineKeyboardButton("🥵 ᴏɴʟʏ ᴀᴅᴜʟᴛꜱ 🙈", url="https://t.me/Pakkinte_Anty_Bitlu")
        ],
        [
            InlineKeyboardButton("⪦ ᴍᴏᴠɪᴇs ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ⪧", url="https://t.me/+37-TDCcQqltlOTRl")
        ]
    ]

    # Create the reply markup with the modified keyboard
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send the message with the inline keyboard
    sent_message = await message.reply_text(
        text="""**__🙂 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴘᴀɴɪɴᴅɪᴀғɪʟᴍᴢ ᴄᴏᴍᴍᴜɴɪᴛʏ!! ᴄʜᴇᴀᴋ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs & ɢʀᴏᴜᴘs ʟɪsᴛ ʙᴇʟᴏᴡ!!__**

**__      ʜᴇ'ʟʟᴏ .. ɪ ᴀᴍ ᴘᴀɴɪɴᴅɪᴀғɪʟᴍᴢ ᴀᴅᴍɪɴ 🤨__**

**__✨  ᴅᴇᴀʟs 𝟸𝟺/𝟽 :- 
@KillerLootDeals __** 

**__✨ ʀᴀʀᴇ ʜɪᴅᴅᴇɴ ᴀᴅᴜʟᴛ ᴍᴏᴠɪᴇs 𝟸.𝟶 
@Telugu_Adults_Rare_Hidden_Movies __**

**__ᴛᴀʀɢᴇᴛ - ʀᴇᴀᴄʜɪɴɢ ᴜʀ sᴇʟғ 🎯__**

**__ғᴏʀ ᴀɴʏ ǫᴜᴇʀɪᴇs - @PIFAdminBot __**

**__ @PanindiaFilmZ 🔥**__""",
        reply_markup=reply_markup
    )
    
    # Delete the sent message and the command message after 10 seconds
    await asyncio.sleep(10)
    await sent_message.delete()
    await message.delete()
