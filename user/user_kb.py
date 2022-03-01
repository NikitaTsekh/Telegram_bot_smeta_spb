from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# Кнопка "Назад"
def user_back_to_main_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Назад', callback_data='user_back_to_main')
            ]
        ]
    )
    return kb


# Что нужно для составления сметы?
def user_smeta_requirement_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Объём работ', callback_data='user_smeta_photo_requirement')
            ],
            [
                InlineKeyboardButton(text='Требования к смете', callback_data='user_smeta_body_requirement')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='user_back_to_main')
            ]
        ]
    )
    return kb


# Кнопка Назад
def user_smeta_requirement_back_kb():
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Назад', callback_data='user_back_to_requirement')
            ]
        ]
    )
    return kb