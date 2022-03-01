from aiogram.utils.exceptions import TypeOfFileMismatch

from admin.admin_mail import send_email
from admin.admin_stat import admin_stat_trigger
from comands_handler_kb import user_ready_kb
from config.config import ADMIN_ID
from functions import bd_set, bd_get_one, bd_get_many
from main import bot, dp, types
from user.user_kb import user_back_to_main_kb, user_smeta_requirement_kb, user_smeta_requirement_back_kb


# Кнопка назад
@dp.callback_query_handler(text_contains='user_back_to_main')
async def user_back_to_main(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    admin_stat_trigger(user_id)

    bd_set(f"UPDATE user_stage SET stage_one = '{0}' WHERE user_id = '{user_id}'")
    text = 'Здравствуйте! Это телеграм-бот smeta-spb.com\n' \
           'Готовы ответить на ваши вопросы'

    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_ready_kb())


# 1 Сколько стоит смета
@dp.callback_query_handler(text_contains='user_smeta_price')
async def user_smeta_price(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "Точную стоимость без задания сказать не можем\n" \
           "Это зависит от:\n\n" \
           "1) Объема исходных данных\n" \
           "2) Подробности исходных данных\n" \
           "3) Требований к смете\n" \
           "4) Будет ли экспертиза\n" \
           "5) Срочность заказа\n\n" \
           "Минимальная смета стоит 3 000.\nСредняя сумма заказа у нас – 8 000 рублей."

    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_back_to_main_kb())


# 2 Как выглядит смета?
@dp.callback_query_handler(text_contains='user_smeta_looks')
async def user_smeta_looks(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    # Проверка наличия фото в базе
    check = bd_get_many(f"SELECT photo FROM smeta_photo WHERE photo != '0'")
    if not check:
        await bot.send_message(user_id, "Фото сметы можно запросить у нас по почте:\n zakaz.smeta-spb@bk.ru")

    else:
        for photo in check:
            # Фото с сжатием
            try:
               await bot.send_document(user_id, photo)

            # Фото без сжатия
            except TypeOfFileMismatch:
                await bot.send_photo(user_id, photo)

        await bot.send_message(user_id, "Вернуться назад /start")


# 3 Кто вы?
@dp.callback_query_handler(text_contains='user_who_u_are')
async def user_who_u_are(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "Мы – команда сметчиков\n" \
           "Руководит командой и составляет сметы Никита Цеханович\n" \
           "Опыт работы – с 2010 года"

    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_back_to_main_kb())


# 4 Что нужно для составления сметы:
@dp.callback_query_handler(text_contains='user_smeta_requirement')
async def user_who_u_are(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "Для составления сметы необходимы:"
    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_smeta_requirement_kb())


# 4.1 Что нужно для составления сметы:
@dp.callback_query_handler(text_contains='user_smeta_photo_requirement')
async def user_who_u_are(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    # Проверка наличия фото в базе
    check = bd_get_many(f"SELECT photo FROM smeta_requirement_photo WHERE photo != '0'")
    if not check:
        await bot.send_message(user_id, "Данные для составления сметы можно запросить у нас по почте:\n"
                                        "zakaz.smeta-spb@bk.ru")

    else:
        for photo in check:
            # Фото с сжатием
            try:
                await bot.send_document(user_id, photo)

            # Фото без сжатия
            except TypeOfFileMismatch:
                await bot.send_photo(user_id, photo)


# 4.2 Что нужно для составления сметы:
@dp.callback_query_handler(text_contains='user_smeta_body_requirement')
async def user_who_u_are(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "В какой сметной базе нужно делать смету?\n" \
           "(Например, ФЕР. Или ТСН г. Москва)\n\n" \
           "Какие индексы?\n" \
           "Если вы не знаете, делаем согласно тому, как принято в вашем регионе"
    await bot.edit_message_text(text, user_id, callback.message.message_id,
                                reply_markup=user_smeta_requirement_back_kb())


# 4.2 Назад:
@dp.callback_query_handler(text_contains='user_back_to_requirement')
async def user_who_u_are(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "Для составления сметы необходимы:"
    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_smeta_requirement_kb())


# 4 Как происходит работа
@dp.callback_query_handler(text_contains='user_work_plan')
async def user_work_plan(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "При заказе от 20 000 по желанию, мы заключаем полноценный договор между вашим ООО и нашим ИП (мы на УСН)\n" \
           "Условия – аванс 50%, 50% по готовности сметы\n\n" \
           "После того как смета готова, мы вам отправляем демо-версию в формате pdf\n" \
           "В случае, если сумма заказа больше 40 000 и будет экспертиза, " \
           "оплата делится на 3 этапа, где 3й этап идет после согласования"

    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_back_to_main_kb())


# 5 КС-2,КС-3
@dp.callback_query_handler(text_contains='user_ks2_ks3')
async def user_ks2_ks3(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "Для этого нужен контракт, чтобы мы взяли оттуда реквизиты" \
           " для заполнения КС2,3 и перенесли смету в программу, после чего делается КС2.3"

    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_back_to_main_kb())


# 6 Нужна коммерческая смета, не в ТЕР ФЕР
@dp.callback_query_handler(text_contains='user_commerce_smeta')
async def user_ks2_ks3(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "К сожалению, такое не делаем, можем только сделать на основании ТЕР/ФЕР"

    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_back_to_main_kb())


# 7 Персональное задание
@dp.callback_query_handler(text_contains='user_personal_q')
async def user_personal_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "Если у вас индивидуальное задание, " \
           "пишите пожалуйста на почту zakaz.smeta-spb@bk.ru или звоните +79215603842"

    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_back_to_main_kb())


# 8 отправка на почту
@dp.callback_query_handler(text_contains='user_email')
async def user_personal_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    admin_stat_trigger(user_id)

    text = "Введите вашу почту:"
    bd_set(f"UPDATE user_stage SET stage_one = '{10}' WHERE user_id = '{user_id}'")

    await bot.edit_message_text(text, user_id, callback.message.message_id, reply_markup=user_back_to_main_kb())


# Сохранение почты
async def user_get_email(message):
    user_id = message.from_user.id

    user_email = str(message.text)

    if user_email.find("@") == -1 or user_email.find(".") == -1:
        await bot.send_message(user_id, "Введите корректный email:")

    else:
        bd_set(f"UPDATE user_stage SET stage_one = 'user_send_email:{message.text}' WHERE user_id = '{user_id}'")
        await bot.send_message(user_id, "Отправьте файл с объёмом работ или спецификацией к проекту:")


# Сохранение почты
async def user_get_doc(message, email):
    user_id = message.from_user.id

    if message.document is not None:
        bd_set(f"UPDATE user_stage SET stage_one = '{0}' WHERE user_id = '{user_id}'")
        send_email(email, message.document)
        await bot.send_message(user_id, "Ваш запрос отправлен на почту\n"
                                        "С вами свяжутся в ближайшее время",
                               reply_markup=user_back_to_main_kb())

    else:
        await bot.send_message(user_id, "Неправильный формат файла\n"
                                        "Отправьте корректный файл:",
                               reply_markup=user_back_to_main_kb())
