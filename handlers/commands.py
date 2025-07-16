from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

command_router = Router()

@command_router.message(Command("start"))
async def start_cmd(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Подписаться за 99⭐", callback_data="subscribe_99")]
    ])
    await message.answer(
        "Подпишитесь, чтобы получать мгновенные уведомления о выходе Новых Подарков Telegram!",
        reply_markup=keyboard
    )

@command_router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer(
        "ℹ️ <b>О боте</b>\n\n"
        "Этот бот уведомляет вас о новых NFT-подарках в Telegram.\n\n"
        "🎯 <b>Особенности:</b>\n"
        "- Автоматические уведомления о новых подарках.\n"
        "- Ручная проверка статуса через меню.\n"
        "- Ежемесячная подписка всего за 99 звёзд Telegram.\n\n"
        "🔄 <b>Как это работает:</b>\n"
        "- Бот проверяет наличие новых подарков каждые 2 секунды.\n"
        "- Как только появятся новые подарки, Вы получите уведомление в этом чате.\n"
        "- Вы всегда можете проверить статус вручную через меню."
    )
