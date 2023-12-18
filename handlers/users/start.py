from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.is_followers import is_followed
from keyboards.default.keybor import menu
from states.register import RegisterState, AdminAnswerState
from utils.db_api.database import Database
from loader import dp, bot
from api_test import translate
from keyboards.inline.channel_list import channel


@dp.message_handler()
async def bot_start(message: types.Message):
    data = translate(message.text)
    await message.answer(data)
