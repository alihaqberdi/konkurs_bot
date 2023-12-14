from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.register import RegisterState, AdminAnswerState
from utils.db_api.database import Database
from loader import dp



@dp.message_handler(lambda message: message.from_user.id == 1737841515)
async def admin_handler(message: types.Message):
    if message.text.startswith("/add_channel"):
        try:
            channel_id = message.text.split()[-1]
            Database(message.from_user.id).add_data("channel-@"+channel_id)
            await message.answer("Kanal qo'shildi")
        except Exception as e:
            await message.answer(f"Xatolik {e}")

