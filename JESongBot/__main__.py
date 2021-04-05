# Infinity BOTs <https://t.me/Infinity_BOTs>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from JESongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from JESongBot import Jebot as app
from JESongBot import LOGGER

pm_start_text = """
Heya [{}](tg://user?id={}), I'm Song Downloader Bot 🎵

Just send me the song name you want , I Will Find For You.
eg: ```/song Believer```

Bot Made By ❤️ @ExploitzBots
"""


@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Channel", url="https://t.me/ExploitzBots"
                    )
                    InlineKeyboardButton(
                        text="Donate", url="https://paypal.me/mushtaq9011"
                    ),
                    InlineKeyboardButton(
                        text="Owner", url="https://t.me/Madboi_xD"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("JESongBot is online.")
idle()
