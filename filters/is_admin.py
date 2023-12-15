from aiogram import types


async def is_add_channel(message: types.Message):
    return message.from_user.id == 1737841515 and message.text.startswith("/add_channel")
