import os
import logging
import asyncio
import instaloader

from dotenv import load_dotenv
from os.path import join, dirname

from dispatcher import bot, dp, L
from aiogram import executor, types

from handlers.start import start_command
from handlers.help import process_help_callback
from handlers.github import process_github_callback
from handlers.download import download_media
from handlers.back import process_back_callback
from handlers.subscription import check_subscription


dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


instagram_username = os.environ.get("username")
instagram_password = os.environ.get("password")


try:
    L.login(instagram_username, instagram_password)
    logging.info(f"🟢 Успешно вошли в Инстаграм как: {instagram_username} %s")
except instaloader.exceptions.ConnectionException as e:
    logging.error(f"🔴 Не удалось войти в Инстаграм: {e} %s")


def register_handlers():
    dp.register_message_handler(start_command, commands=["start"])
    dp.register_callback_query_handler(process_help_callback, lambda c: c.data == "help")
    dp.register_callback_query_handler(process_github_callback, lambda c: c.data == "github")
    dp.register_callback_query_handler(process_back_callback, lambda c: c.data == "back")
    dp.register_callback_query_handler(check_subscription, lambda query: query.data == "check_subscription")
    dp.register_message_handler(download_media, content_types=["text"])


async def set_commands():
    commands = [
        types.BotCommand(command="/start", description="Начать")
    ]
    await bot.set_my_commands(commands)


if __name__ == "__main__":
    register_handlers()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_commands())
    executor.start_polling(dp, skip_updates=True)
