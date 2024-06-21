from aiogram import types
from dispatcher import dp, bot, channel_id


@dp.callback_query_handler(lambda query: query.data == "check_subscription")
async def check_subscription(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    try:
        channel_member = await bot.get_chat_member(channel_id, user_id)
        if channel_member.status == "member":
            await bot.answer_callback_query(
                callback_query.id,
                text="🟢 Теперь вы можете использовать бот!\n🥰 Спасибо что выбрали нас!\n\n😇 Пожалуйста повторите свой запрос:)",
                show_alert=True
            )
            await bot.delete_message(
                chat_id=callback_query.message.chat.id,
                message_id=callback_query.message.message_id
            )
        else:
            await bot.answer_callback_query(
                callback_query.id,
                text="🔴 Вы не подписаны на телеграм канал!",
                show_alert=True
            )
    except Exception as e:
        print(e)
