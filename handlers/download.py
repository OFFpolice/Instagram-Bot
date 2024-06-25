import instaloader
from aiogram import types
from dispatcher import dp, bot, L, channel_id, channel_link, photo_link


@dp.message_handler(regexp=r"https://www\.instagram\.com/(p|reel)/")
async def download_media(message: types.Message):
    channel_member = await bot.get_chat_member(channel_id, message.chat.id)
    if channel_member.status == "left":
        status_button = types.InlineKeyboardMarkup()
        status_button.add(
            types.InlineKeyboardButton(
                text="Подписаться",
                url=channel_link
            )
        )
        status_button.row(
            types.InlineKeyboardButton(
                text="Проверка",
                callback_data="check_subscription"
            )
        )
        await bot.send_photo(
            chat_id=message.chat.id,
            photo=photo_link,
            caption="<b>🔒 Для доступа к функциям бота, подпишитесь на канал!\n\nПосле подписки вернитесь в диалог с ботом и нажмите кнопку «Проверка».\nЗатем повторите свой запрос!</b>",
            parse_mode="HTML",
            reply_markup=status_button
        )
        await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
        return
    
    message_sticker = await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEL4ahmFZL-mpr6JHYpjetNsXYZZt3raAACIwADKA9qFCdRJeeMIKQGNAQ")
    processing_message = await bot.send_message(chat_id=message.chat.id, text="<b>Пожалуйста, подождите!</b>\n<b><i>Загрузка началась...</i></b>", parse_mode="HTML")
    
    try:
        shortcode = message.text.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        media_group = []

        if post.mediacount > 1:
            for node in post.get_sidecar_nodes():
                if node.is_video:
                    await bot.send_chat_action(chat_id=message.chat.id, action="upload_video")
                    media_group.append(types.InputMediaVideo(media=node.video_url))
                else:
                    await bot.send_chat_action(chat_id=message.chat.id, action="upload_photo")
                    media_group.append(types.InputMediaPhoto(media=node.display_url))
        else:
            if post.is_video:
                await bot.send_chat_action(chat_id=message.chat.id, action="upload_video")
                media_group.append(types.InputMediaVideo(media=post.video_url))
            else:
                await bot.send_chat_action(chat_id=message.chat.id, action="upload_photo")
                media_group.append(types.InputMediaPhoto(media=post.url))

        post_text = post.caption
        original_url = f"https://www.instagram.com/p/{shortcode}/"
        profile_url = f"https://www.instagram.com/{post.owner_username}/"
        info_message = (
            f"{post_text}\n\n"
            f"<b>🔗 Ссылка на <a href='{original_url}'>публикацию</a></b>\n"
            f"<b>👤 Ссылка на <a href='{profile_url}'>профиль</a></b>\n\n"
        )
        
        chunk_size = 10
        for i in range(0, len(media_group), chunk_size):
            chunk = media_group[i:i + chunk_size]
                
            if isinstance(chunk[0], types.InputMediaPhoto):
                chunk[0].caption = info_message
                chunk[0].parse_mode = "HTML"
            elif isinstance(chunk[0], types.InputMediaVideo):
                chunk[0].caption = info_message
                chunk[0].parse_mode = "HTML"

            await bot.send_media_group(chat_id=message.chat.id, media=chunk)

        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=message_sticker.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
        
    except Exception as e:
        await bot.send_message(chat_id=message.chat.id, text=f"<b>Произошла ошибка при загрузке:</b> <code>{e}</code>", parse_mode="HTML")
        print(e)

        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=message_sticker.message_id)
        await bot.delete_message(chat_id=message.chat.id, message_id=processing_message.message_id)
