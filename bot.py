import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config_reader import get_config, BotConfig
from dispatcher import dp

async def main():
    bot_config: BotConfig = get_config(model=BotConfig, root_key="bot")
    bot = Bot(
        token=bot_config.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())