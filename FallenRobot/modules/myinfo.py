from telethon import events, Button, custom, version
from telethon.tl.types import ChannelParticipantsAdmins
import asyncio
import os,re
import requests
import datetime
import time
from datetime import datetime
import random
from PIL import Image
from io import BytesIO
from FallenRobot import telethn as bot
from FallenRobot import telethn as tgbot
from FallenRobot.events import register
from FallenRobot import dispatcher


edit_time = 5
""" =======================FALLEN ROBOT====================== """
file1 = "https://telegra.ph/file/a961411720d1e7498b8c6.jpg"
file2 = "https://telegra.ph/file/46c96bc757260485b46da.jpg"
file3 = "https://telegra.ph/file/8e9b5acd0e2d76a39bba7.jpg"
file4 = "https://telegra.ph/file/fe2cb7ae42e30a2b8c42a.jpg"
file5 = "https://telegra.ph/file/c641abcfbd0169b7ed48e.jpg"
""" =======================FALLEN ROBOT====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    chat = await event.get_chat()
    current_time = datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information",data="informations")]]
    on = await bot.send_file(event.chat_id, file=file2,caption= f"Hey {firstname}, \n Click on the button below \n to get info about you", buttons=button)

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button) 

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    LILIE = "POWERED BY 𝘔𝘙 𝘚𝘏𝘌𝘓𝘉𝘠 \n\n"
    LILIE += f"FIRST NAME : {PRO.first_name} \n"
    LILIE += f"LAST NAME : {PRO.last_name}\n"
    LILIE += f"YOU BOT : {PRO.bot} \n"
    LILIE += f"RESTRICTED : {PRO.restricted} \n"
    LILIE += f"USER ID : {boy}\n"
    LILIE += f"USERNAME : {PRO.username}\n"
    await event.answer(LILIE, alert=True)
  except Exception as e:
    await event.reply(f"{e}")


__command_list__ = [
    "myinfo"
]
