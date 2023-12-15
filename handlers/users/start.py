from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.is_followers import is_followed
from keyboards.default.keybor import menu
from states.register import RegisterState, AdminAnswerState
from utils.db_api.database import Database
from loader import dp, bot
from keyboards.inline.channel_list import channel


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not await is_followed(message.from_user.id):
        await message.answer(f"kanallarga azo bo'ling", reply_markup=channel)
        return
    ball = 0

    user_id = message.text.split()[-1]
    print(user_id)
    data = Database(message.from_user.id)
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} botimizga xush kelibsiz", reply_markup=menu)
