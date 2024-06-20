from aiogram import types
from dispatcher import dp, bot, video_link


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("🌀 Shazam Bot", url="https://telegram.me/OFFpoliceShazamBot"),
        types.InlineKeyboardButton("🆘 Помощь", callback_data="help")
    )
    await bot.send_video(
        chat_id=message.chat.id,
        video=video_link,
        caption=f"<b>👋 Привет, {message.chat.first_name}!</b>\n\nС помощью этого бота вы сможете скачивать медиа из <b><i>«Instagram»</i></b>!\n\nСкопируйте ссылку на медиа из <b><i>«Instagram»</i></b> и пришлите мне!\n\n<b><i>Это может быть видео, фото! 📸📹</i></b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )
    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id
    )
