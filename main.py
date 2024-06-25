import os
import logging
import asyncio
import instaloader

from dotenv import load_dotenv
from os.path import join, dirname

from dispatcher import dp, bot, L
from aiogram import executor, types

from handlers.start import start_command
from handlers.help import help_callback
from handlers.back import back_callback
from handlers.subscription import check_subscription
from handlers.download import download_media
from handlers.profile import download_profile


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


instagram_username = os.environ.get("username")
instagram_password = os.environ.get("password")


try:
    L.login(instagram_username, instagram_password)
    logging.info(f"🟢 Успешно вошли в Инстаграм как: {instagram_username} %s")
except instaloader.exceptions.ConnectionException as e:
    logging.error(f"🔴 Не удалось войти в Инстаграм: {e} %s")


async def register_handlers():
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_callback_query_handler(help_callback, lambda c: c.data == "help")
    dp.register_callback_query_handler(back_callback, lambda c: c.data == "back")
    dp.register_callback_query_handler(check_subscription, lambda query: query.data == "check_subscription")
    dp.register_message_handler(download_media, regexp=r"https://www\.instagram\.com/(p|reel)/")
    dp.register_message_handler(download_profile, regexp=r"https?://(www\.)?instagram\.com/([^/?]+)")


async def set_commands():
    commands = [
        types.BotCommand(command="/start", description="🤖 Start")
    ]
    await bot.set_my_commands(commands)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(register_handlers())
    loop.run_until_complete(set_commands())
    executor.start_polling(dp, skip_updates=True)
