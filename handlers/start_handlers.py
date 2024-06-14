from aiogram import types
from dispatcher import dp, bot, video_link


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    url_button = types.InlineKeyboardButton("🌀 Shazam Bot", url="https://telegram.me/OFFpoliceShazamBot")
    help_button = types.InlineKeyboardButton("🆘 Помощь", callback_data="help")
    markup.add(url_button, help_button)
    await bot.send_video(
        chat_id=message.chat.id,
        video=video_link,
        caption=f"<b>Здравствуйте, {message.chat.first_name}!</b>\n\nС помощью этого бота вы сможете скачивать медиа из <b><i>«Instagram»</i></b>!\n\nСкопируйте ссылку на медиа из <b><i>«Instagram»</i></b> и пришлите мне!\n\n<b><i>Это может быть видео, фото! 📸📹</i></b>",
        parse_mode="HTML",
        reply_markup=markup
    )
