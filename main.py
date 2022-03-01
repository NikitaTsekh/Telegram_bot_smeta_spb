

import asyncio
from aiogram import Bot, Dispatcher, executor, types

from admin.admin_mail import send_email
from config import config

# Инициализация бота
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)


if __name__ == '__main__':
    from comands_handlers import dp
    from message_handler import dp
    from admin.admin_handler import dp
    from user.user_handler import dp
    from admin.admin_stat import dp


    executor.start_polling(dp, skip_updates=True)


