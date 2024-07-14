import os
import logging
import aiohttp
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
bot_token = os.environ.get("bot_token")


bot = Bot(token=bot_token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())
logging.basicConfig(level=logging.INFO)
L = instaloader.Instaloader()


async def bot_username():
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
            if result["ok"]:
                bot_info = result["result"]
                return bot_info["username"]
    return None
