from aiogram import types

from filters.is_admin import is_add_channel
from keyboards.default.keybor import menu
from keyboards.inline.channel_list import profile_inline
from loader import dp, bot
from utils.db_api.database import Database


@dp.message_handler(is_add_channel)
async def admin_handler(message: types.Message):
    try:
        channel_id = message.text.split()[-1]
        await bot.get_chat_member(f"@{channel_id}", message.from_user.id)
        Database(message.from_user.id).add_data("channel-@" + channel_id)
        await message.answer("Kanal qo'shildi")
    except Exception as e:
        await message.answer(f"Xatolik {e}")


@dp.message_handler(text='Profile')
async def profile_handler(message: types.Message):
    data = Database(message.from_user.id)
    await message.answer(f"Your profile:\n"
                         f"ballar: {99}\n"
                         f"o'rin: {99}\n"
                         f"`referal: https://t.me/obhavo_weather_pagodabot?start={message.from_user.id}`\n"
                         , reply_markup=profile_inline, parse_mode="Markdown")
