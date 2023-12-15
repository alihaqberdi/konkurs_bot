from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Profile"), KeyboardButton(text="Reyting")],
        [KeyboardButton(text="Konkurs haqida")],
    ], resize_keyboard=True
)


