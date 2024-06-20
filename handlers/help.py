from aiogram import types
from dispatcher import dp, bot


@dp.callback_query_handler(lambda c: c.data == "help")
async def process_help_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton("📦 GitHub", callback_data="github"),
        types.InlineKeyboardButton("🔙 Назад", callback_data="back")
    )
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption="<b>⁉️ Если вы хотите скачать медиа с платформы «Instagram» вам нужно будет следовать этой инструкции:</b>\n\n<b>1. Для этого откройте приложение «Instagram» найдите интересующее вас медиа и нажмите кнопку «Поделиться».</b>\n<i>Затем выберите опцию «Копировать ссылку».</i>\n<b>2. Отправьте скопированную ссылку чат-боту.</b>\n<i>Вставьте ссылку в поле сообщения и отправьте боту.</i>\n<b>3. Бот обработает предоставленную ссылку и предоставит вам медиа.</b>\n<i>Размер медиа будет ограничен (20Мб)</i>.",
        parse_mode="HTML",
        reply_markup=keyboard
    )
