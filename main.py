import os
import logging
import asyncio
import instaloader

from dotenv import load_dotenv
from os.path import join, dirname

from dispatcher import dp, L
from aiogram import executor
from handlers import register_handlers


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


instagram_username = os.environ.get("username")
instagram_password = os.environ.get("password")


try:
    L.login(instagram_username, instagram_password)
    logging.info(f"🟢 Успешно вошли в Инстаграм как: {instagram_username} %s")
except instaloader.exceptions.ConnectionException as e:
    logging.error(f"🔴 Не удалось войти в Инстаграм: {e} %s")


register_handlers(dp)


if __name__ == "__main__":
    asyncio.run(executor.start_polling(dp, skip_updates=True))
