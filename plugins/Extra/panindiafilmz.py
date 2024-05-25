from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

CMD = ["/", "."]

Client.on_message(filters.command("PanindiaFilmZ", CMD))
async def PanindiaFilmZ_command(_, m: Message):
    try:
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
        await m.reply(
            """**🙃 __Welcome To My PanindiaFilmZ Community!! Cheak Our Channels & Groups List Below!!**__

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
 
    except Exception as e:
        print(f"Error: {e}")
