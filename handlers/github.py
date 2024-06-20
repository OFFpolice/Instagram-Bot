from aiogram import types
from dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == "github")
async def process_github_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("📦 GitHub Repository", url="https://github.com/OFFpolice/Instagram-Bot"),
        types.InlineKeyboardButton("👤 GitHub Profile", url="https://github.com/OFFpolice"),
        types.InlineKeyboardButton("🔙 Главная", callback_data="back")
    )
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption="<b><a href='https://github.com/OFFpolice/Instagram-Bot'>👾 Исходный код! 👾</a></b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )
