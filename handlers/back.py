from aiogram import types
from dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == "back")
async def back_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("🌀 Shazam Bot", url="https://telegram.me/OFFpoliceShazamBot"),
        types.InlineKeyboardButton("🔁 Поделиться", url="https://t.me/share/url?url=https://t.me/Save_InstagramBot&text=👋%20Привет,%20я%20нашел%20классного%20бота%20с%20помощью%20которого%20можно%20сохранять%20видео%20и%20фотографии%20из%20Instagram%20прямо%20в%20Telegram"),
        types.InlineKeyboardButton("🆘 Помощь", callback_data="help")
    )
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=f"<b>👋 Здравствуйте, {callback_query.from_user.first_name}!</b>\n\nС помощью этого бота вы сможете скачивать медиа из <b>«Instagram»</b>!\n\nСкопируйте ссылку на медиа из <b>«Instagram»</b> и пришлите мне!\n\n<b>Это может быть видео, фото! 📸📹</b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )
