from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from functions import bd_get_many


# Кнопка в выборе фото
def admin_smeta_photo_kb():
    kb = InlineKeyboardMarkup()
    count = 1

    buttons = bd_get_many(f"SELECT photo FROM smeta_photo")
    for button in buttons:
        if button == '0':
            text = "[ПУСТО]"
        else:
            text = f"[ФОТО {count}]"

        kb.add(types.InlineKeyboardButton(text=text, callback_data=f"admin_smeta_baby_photo:{count}"))
        count += 1
    return kb


# Добавить фото
def admin_smeta_add_photo_kb(photo_id):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Добвить фото', callback_data=f'admin_smeta_add_photo:{photo_id}')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='admin_smeta_add_back')
            ]
        ]
    )
    return kb


# Редактировать / удалить фото
def admin_smeta_change_photo_kb(photo_id):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Редактировать фото', callback_data=f'admin_smeta_add_photo:{photo_id}')
            ],
            [
                InlineKeyboardButton(text='Удалить фото', callback_data=f'admin_smeta_del_photo:{photo_id}')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='admin_smeta_add_back')
            ]
        ]
    )
    return kb


#
# Что нужно для составления сметы
# Кнопка в выборе фото
def admin_smeta_requirement_photo_kb():
    kb = InlineKeyboardMarkup()
    count = 1

    buttons = bd_get_many(f"SELECT photo FROM smeta_requirement_photo")
    for button in buttons:
        if button == '0':
            text = "[ПУСТО]"
        else:
            text = f"[ФОТО {count}]"

        kb.add(types.InlineKeyboardButton(text=text, callback_data=f"admin_smeta_requirement_baby_photo:{count}"))
        count += 1
    return kb


# Добавить фото
def admin_smeta_requirement_add_photo_kb(photo_id):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Добвить фото', callback_data=f'admin_smeta_requirement_add_photo:{photo_id}')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='admin_smeta_requirement_add_back')
            ]
        ]
    )
    return kb


# Редактировать / удалить фото
def admin_smeta_requirement_change_photo_kb(photo_id):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Редактировать фото', callback_data=f'admin_smeta_requirement_add_photo:{photo_id}')
            ],
            [
                InlineKeyboardButton(text='Удалить фото', callback_data=f'admin_smeta_requirement_del_photo:{photo_id}')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='admin_smeta_requirement_add_back')
            ]
        ]
    )
    return kb



