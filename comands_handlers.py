from admin.admin_stat import admin_stat_trigger
from comands_handler_kb import admin_main_kb, user_ready_kb
from config.config import ADMIN_ID
from functions import bd_get_one, bd_set
from main import bot, dp, types
import random


# Обработчик команды 'Start'
@dp.message_handler(commands=['start'])
async def send_welcome(message):
    user_id = message.from_user.id
    admin_stat_trigger(user_id)

    check = bd_get_one(f"SELECT user_id FROM user_stage WHERE user_id = '{user_id}'")
    if check is None:
        bd_set(f"INSERT INTO user_stage VALUES('{user_id}', '{0}', '{0}', '{0}')")

    # Проверка на администратора
    if f'{user_id}' in ADMIN_ID:
        await bot.send_message(user_id, 'Открыта панель администратора', reply_markup=admin_main_kb())

    else:
        await bot.send_message(user_id, 'Здравствуйте! Это телеграм-бот smeta-spb.com\n'
                                        'Готовы ответить на ваши вопросы', reply_markup=user_ready_kb())
