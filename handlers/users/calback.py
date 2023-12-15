from aiogram import types

from keyboards.default.keybor import menu
from loader import dp, bot
from utils.db_api.database import Database


@dp.callback_query_handler(text="check")
async def check_channels_join(call: types.CallbackQuery):
    data = Database(call.from_user.id)
    channels = data.get_channels()
    for channel in channels:
        status = await bot.get_chat_member(f"{channel[:-1]}", call.from_user.id)
        if status.status not in ["member", "creator", "administrator"]:
            await call.answer("Kanalga azo bo'ling", show_alert=True)
            return False
    await call.message.answer("Assalomu alaykum konkurs botiga xush kelibsiz", reply_markup=menu)
    await call.message.delete()
    return True
