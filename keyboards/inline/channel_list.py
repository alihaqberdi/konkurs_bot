from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.db_api.database import Database

data = Database(1737841515)
print(data.get_channels())
channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text=f"Kanalga obuna {i}", url="https://t.me/" + data[1:])] for i, data in
        enumerate(data.get_channels(), start=1)
    ]
)
