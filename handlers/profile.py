import re
import asyncio
from aiogram import types
from dispatcher import dp, bot, L
from instaloader import Profile


@dp.message_handler(regexp=r"https?://(www\.)?instagram\.com/([^/?]+)")
async def download_profile(message: types.Message):
    url = message.text.strip()
    match = re.search(r"https?://(www\.)?instagram\.com/([^/?]+)", url)
    if match:
        username = match.group(2)
        message_sticker = await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEL4ahmFZL-mpr6JHYpjetNsXYZZt3raAACIwADKA9qFCdRJeeMIKQGNAQ")
        processing_message = await bot.send_message(chat_id=message.chat.id, text="<b>Пожалуйста, подождите!</b>\n<b><i>Загрузка информации о профиле...⏳⌛️⏳⌛️</i></b>", parse_mode="HTML")
        
        try:
            profile = await asyncio.to_thread(Profile.from_username, L.context, username)
            profile_info = (
                f"👤 <b>Название:</b> {profile.full_name or 'Не указано'}\n"
                f"🆔 <b>Пользователь:</b> <a href=\"{url}\">@{profile.username}</a>\n"
                f"👥 <b>Подписчиков:</b> {profile.followers}\n"
                f"✅ <b>Верифицирован:</b> {'Да' if profile.is_verified else 'Нет'}"
            )
            
            keyboard = types.InlineKeyboardMarkup(row_width=1)
            keyboard.add(
                types.InlineKeyboardButton(f"{profile.username}", url=f"{url}"),
                types.InlineKeyboardButton("🌀 Shazam Bot", url="https://telegram.me/OFFpoliceShazamBot")
            )
            
            await bot.send_photo(chat_id=message.chat.id, photo=profile.profile_pic_url, caption=profile_info, reply_markup=keyboard, parse_mode="HTML")
            
        except Exception as e:
            await bot.send_message(chat_id=message.chat.id, text=f"<b>❌ Не удалось получить информацию о профиле.</b>\n<b>Ошибка:</b> <code>{e}</code>", parse_mode="HTML")
        
        finally:
            await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
            await bot.delete_message(chat_id=message.chat.id, message_id=message_sticker.message_id)
            await bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
    else:
        await bot.send_message(chat_id=message.chat.id, text="<b>❌ Неправильный URL профиля Instagram.</b>", parse_mode="HTML")
