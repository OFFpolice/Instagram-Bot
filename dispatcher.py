import os
import logging
import instaloader

from dotenv import load_dotenv
from os.path import join, dirname

from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


channel_link = os.environ.get("channel_link")
channel_id = os.environ.get("channel_id")
photo_link = os.environ.get("photo_link")
video_link = os.environ.get("video_link")
bot_name = os.environ.get("bot_name")
bot_token = os.environ.get("bot_token")


bot = Bot(token=bot_token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)
L = instaloader.Instaloader()
