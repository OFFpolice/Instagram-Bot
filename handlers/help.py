from aiogram import types
from dispatcher import dp, bot


@dp.callback_query_handler(lambda query: query.data == "help")
async def help_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton("🌀 Shazam Bot", url="https://t.me/OFFpoliceShazamBot"),
        types.InlineKeyboardButton("🔁 Поделиться", url="https://t.me/share/url?url=https://t.me/Save_InstagramBot&text=👋%20Привет,%20сохраняй%20видео%20и%20фотографии%20из%20Instagram%20прямо%20в%20Telegram%20😏😏😏"),
        types.InlineKeyboardButton("🔙 Назад", callback_data="back")
    )
    await bot.edit_message_caption(
        chat_id=callback_query.message.chat.id,
        message_id=callback_query.message.message_id,
        caption="<b>⁉️ Если вы хотите скачать медиа с платформы «Instagram» вам нужно будет следовать этой инструкции:</b>\n\n<b>1.</b> Для этого откройте приложение <b>«Instagram»</b> найдите интересующее вас медиа и нажмите кнопку <b>«Поделиться»</b>.\nЗатем выберите опцию <b>«Копировать ссылку»</b>.\n<b>2.</b> Отправьте скопированную ссылку чат-боту.\nВставьте ссылку в поле <b>«Сообщение»</b> и отправьте боту.\n<b>3.</b> Бот обработает предоставленную ссылку и предоставит вам медиа.\nРазмер медиа будет ограничен <b><a href=\'https://core.telegram.org/bots/faq#how-do-i-download-files'>20mb</a></b>, узнать про ограничения <b><a href=\'https://core.telegram.org/bots/api'>Telegram Bot API</a></b>.\n\n<b>‼️ Обратите внимание, что загрузка контента, защищенного авторским правом, без разрешения является уголовным преступлением.\n‼️ Убедитесь, что вы загружаете только свой собственный контент или контент, на загрузку которого у вас есть разрешение.</b>",
        parse_mode="HTML",
        reply_markup=keyboard
    )
