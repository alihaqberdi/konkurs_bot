from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.database import Database

data = Database(1737841515)

check = InlineKeyboardButton(text="Tekshirish", callback_data="check")

channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=f"Kanalga obuna {i}", url="https://t.me/" + data[1:])] for i, data in
        enumerate(data.get_channels(), start=1)
    ]
)
channel.add(check)

profile_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="back", callback_data="back")
        ]
    ]
)
