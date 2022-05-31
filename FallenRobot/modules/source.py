from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


ANON = "https://telegra.ph/file/48761c4d8df1797825af9.jpg"

@client.on_message(filters.command(["repo", "source"]))
async def repo(client, message):
    await message.reply_photo(
        photo=ANON,
        caption=f"""**ʜᴇʏ​ {message.from_user.mention()},\n\nɪ ᴀᴍ [ᴀɴɢᴇʟ ✘ ʀᴏʙᴏᴛ-🇮🇩](t.me/AngelxRobot)**

**» ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ :** [𝘔𝘙 𝘚𝘏𝘌𝘓𝘉𝘠](tg://user?id=2005952005)
**» ᴩʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**» ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}` 
**» ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}` 
**» ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴀɴɢᴇʟ ✘ ʀᴏʙᴏᴛ sᴏᴜʀᴄᴇ ɪᴢ ᴘᴠᴛ ᴜ ᴄᴀɴ ᴊᴏɪɴ ʜᴇʀᴇ ꜰᴏʀ ʀᴇᴘᴏ @angelsupports.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• ᴏᴡɴᴇʀ •", url="tg://user?id=2005952005"), 
                    InlineKeyboardButton(
                        "• sᴏᴜʀᴄᴇ •", url="https://github.com")
                ]
            ]
        )
    )

__mod_name__ = "Rᴇᴩᴏ"
