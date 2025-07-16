from aiogram import Dispatcher
from handlers.donate import donate_router
from handlers.commands import command_router

dp = Dispatcher()
dp.include_routers(command_router, donate_router)