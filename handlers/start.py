from aiogram import types
from dispatcher import dp, bot, video_link


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("🌀 Shazam Bot", url="https://t.me/OFFpoliceShazamBot"),
        types.InlineKeyboardButton("🔁 Поделиться", url="https://t.me/share/url?url=https://t.me/Save_InstagramBot&text=👋%20Привет,%20я%20нашел%20классного%20бота%20с%20помощью%20которого%20можно%20сохранять%20видео%20и%20фотографии%20из%20Instagram%20прямо%20в%20Telegram"),
        types.InlineKeyboardButton("🆘 Помощь", callback_data="help")
    )
    await bot.send_video(
        chat_id=message.chat.id,
        video=video_link,
        caption=f"<b>👋 Здравствуйте, {message.chat.first_name}!</b>\n\nС помощью этого бота вы сможете скачивать медиа из <b>«Instagram»</b>!\n\nСкопируйте ссылку на медиа из <b>«Instagram»</b> и пришлите мне!\n\n<b>Это может быть видео, фото! 📸📹</b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id
    )
