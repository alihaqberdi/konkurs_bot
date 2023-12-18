from aiogram import Dispatcher

from loader import dp
from .throttling import MyMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(MyMiddleware())

