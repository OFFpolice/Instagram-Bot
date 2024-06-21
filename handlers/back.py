from aiogram import types
from dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == "back")
async def process_back_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("🌀 Shazam Bot", url="https://telegram.me/OFFpoliceShazamBot"),
        types.InlineKeyboardButton("🆘 Помощь", callback_data="help")
    )
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption=f"<b>👋 Здравствуйте, {callback_query.from_user.first_name}!</b>\n\nС помощью этого бота вы сможете скачивать медиа из <b><i>«Instagram»</i></b>!\n\nСкопируйте ссылку на медиа из <b><i>«Instagram»</i></b> и пришлите мне!\n\n<b><i>Это может быть видео, фото! 📸📹</i></b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )
