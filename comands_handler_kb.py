from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# admin_main_kb
def admin_main_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Как выглядит смета - фото', callback_data='admin_smeta_photo'),
            ],
            [
                InlineKeyboardButton(text='Что нужно для составления сметы- фото',
                                     callback_data='admin_requirement_photo'),
            ],
            [
                InlineKeyboardButton(text='Тестовый запуск', callback_data='admin_test_run')
            ],
            [
                InlineKeyboardButton(text='Стасистика', callback_data='admin_get_stat')
            ],
            [
                InlineKeyboardButton(text='Пробная кнопка!!!!', callback_data='admin_test_run')
            ]
        ]
    )
    return kb


# user_ready_kb
def user_ready_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Сколько стоит смета?', callback_data='user_smeta_price'),
            ],
            [
                InlineKeyboardButton(text='Как выглядит смета?', callback_data='user_smeta_looks')
            ],
            [
                InlineKeyboardButton(text='Что нужно для составления сметы?', callback_data='user_smeta_requirement')
            ],
            [
                InlineKeyboardButton(text='Кто вы?', callback_data='user_who_u_are')
            ],
            [
                InlineKeyboardButton(text='Как происходит работа?', callback_data='user_work_plan')
            ],
            [
                InlineKeyboardButton(text='КС-2, КС-3', callback_data='user_ks2_ks3')
            ],
            [
                InlineKeyboardButton(text='Нужна коммерческая смета, не в ТЕР ФЕР', callback_data='user_commerce_smeta')
            ],
            [
                InlineKeyboardButton(text='Другое (индивидуальное задание)', callback_data='user_personal_q')
            ],
            [
                InlineKeyboardButton(text='Отправить объём работ или спецификацию к проекту', callback_data='user_email')
            ]
        ]
    )
    return kb