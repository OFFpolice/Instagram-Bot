from aiogram import types
from dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == "github")
async def process_github_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("📦 GitHub Repository", url="https://github.com/OFFpolice/Instagram-Downloads-Telegram-Bot"),
        types.InlineKeyboardButton("👤 GitHub Profile", url="https://github.com/OFFpolice"),
        types.InlineKeyboardButton("🔙 Главная страница", callback_data="back")
    )
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption="<b>👾 Привет, технологические маги и поклонники цифрового искусства! 👾</b>\n\nПриглашаю вас в удивительный мир моего <a href='https://github.com/OFFpolice'>GitHub профиля</a>, где обитают необычные разработки! Особенно рекомендую взглянуть на <a href='https://github.com/OFFpolice/Instagram-Downloads-Telegram-Bot'>репозиторий</a> с Телеграм-ботом, который умеет загружать видео и фото прямо из Instagram 📸📹.\n\nЕсли вам нравится магия кода, поставьте звезду ⭐ и присоединяйтесь к приключению. Вместе мы можем творить цифровые чудеса!\n\n<b><a href='https://github.com/OFFpolice/Instagram-Downloads-Telegram-Bot'>👉 Исходный код бота! 👈</a></b>\n\n<b>До встречи на GitHub! 🚀✨</b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )
