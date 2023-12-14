from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.register import RegisterState, AdminAnswerState
from utils.db_api.database import Database


from loader import dp
from keyboards.inline.channel_list import channel


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom menga savolingiz bo'lsa ismingizni yuboring" ,reply_markup=channel)
    data = Database(message.from_user.id)
    await RegisterState.name.set()


