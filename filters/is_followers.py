from aiogram import types

from loader import bot
from utils.db_api.database import Database


async def is_followed(user_id):
    data = Database(user_id)
    channels = data.get_channels()
    for channel in channels:
        status = await bot.get_chat_member(f"{channel[:-1]}", user_id)
        if status.status not in ["member", "creator", "administrator"]:
            return False
    return True
