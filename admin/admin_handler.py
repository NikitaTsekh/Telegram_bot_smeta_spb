from aiogram.utils.exceptions import TypeOfFileMismatch

from admin.admin_kb import admin_smeta_photo_kb, admin_smeta_add_photo_kb, admin_smeta_change_photo_kb, \
    admin_smeta_requirement_photo_kb, admin_smeta_requirement_add_photo_kb, admin_smeta_requirement_change_photo_kb
from comands_handler_kb import admin_main_kb, user_ready_kb
from config.config import ADMIN_ID, BOT_TOKEN
from functions import bd_set, bd_get_one
from main import bot, dp, types


# Как выглядит смета - актуальные фото
@dp.callback_query_handler(text_contains='admin_smeta_photo')
async def admin_main_kb_new_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    # Проверка на наличие сслотов под фото
    check = bd_get_one(f"SELECT photo_id FROM smeta_photo WHERE photo_id = '{1}'")

    # [ПУСТО]
    if check is None:
        for i in range(5):
            bd_set(f"INSERT INTO smeta_photo VALUES('{i + 1}', '{0}')")

    # Отправка сообщения пользователю
    text = 'Фото, которые будут отправляться пользователю при нажатии\n"Как выглядит смета?"'
    await bot.send_message(user_id, text, reply_markup=admin_smeta_photo_kb())


# Как выглядит смета - просмотр фото и редактирование
@dp.callback_query_handler(text_contains='admin_smeta_baby_photo:')
async def admin_main_kb_new_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    data = str(callback.data)

    # Проверка на наличие фото
    photo_id = data.replace("admin_smeta_baby_photo:", "")
    check = bd_get_one(f"SELECT photo FROM smeta_photo WHERE photo_id = '{photo_id}'")
    if check == '0':
        text = "Фото не загружено\n" \
               "Возможные действия:"
        await bot.send_message(user_id, text, reply_markup=admin_smeta_add_photo_kb(photo_id))

    # [Фото]
    else:
        # Фото с сжатием
        try:
            await bot.send_document(user_id, check, reply_markup=admin_smeta_change_photo_kb(photo_id))

        # Фото без сжатия
        except TypeOfFileMismatch:
            await bot.send_photo(user_id, check, reply_markup=admin_smeta_change_photo_kb(photo_id))


# Как выглядит смета - добавить фото
@dp.callback_query_handler(text_contains='admin_smeta_add_photo:')
async def admin_main_kb_new_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    photo_id = str(callback.data).replace("admin_smeta_add_photo:", "")

    print(1)
    bd_set(f"UPDATE user_stage SET stage_one = 'adm_set_photo:{photo_id}' WHERE user_id = '{user_id}'")
    await bot.send_message(user_id, "Отправьте фото:")


# Сохранение фото
async def admin_smeta_add_photo(message, photo_id):
    print(photo_id)
    user_id = message.from_user.id
    photo_id = str(photo_id).replace("adm_set_photo:", "")

    # Фото с сжатием
    try:
        await bot.send_document(user_id, message.document.file_id)
        bd_set(f"UPDATE smeta_photo SET photo = '{message.document.file_id}' WHERE photo_id = '{photo_id}'")
        bd_set(f"UPDATE user_stage SET stage_one = '{0}' WHERE user_id = '{user_id}'")
        text = "Сообщение сохранено"
        await bot.send_message(user_id, text)

    # Фото без сжатия
    except AttributeError:
        try:
            await bot.send_photo(user_id, message.photo[-1].file_id)
            bd_set(f"UPDATE smeta_photo SET photo = '{message.photo[-1].file_id}' WHERE photo_id = '{photo_id}'")
            bd_set(f"UPDATE user_stage SET stage_one = '{0}' WHERE user_id = '{user_id}'")
            text = "Сообщение сохранено"
            await bot.send_message(user_id, text)

    # Ошибка
        except IndexError:
            await bot.send_message(user_id, "Неправильный формат, отправьте фото или документ:")


# Как выглядит смета - удалить фото
@dp.callback_query_handler(text_contains='admin_smeta_del_photo:')
async def admin_main_kb_new_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    data = str(callback.data)
    photo_id = str(data).replace("admin_smeta_del_photo:", "")

    bd_set(f"UPDATE smeta_photo SET photo = '{0}' WHERE photo_id = '{photo_id}'")
    await bot.send_message(user_id, "Фото удлено")


#
# Что нужно для составления сметы - актуальные фото
@dp.callback_query_handler(text_contains='admin_requirement_photo')
async def admin_main_kb_new_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    # Проверка на наличие сслотов под фото
    check = bd_get_one(f"SELECT photo_id FROM smeta_requirement_photo WHERE photo_id = '{1}'")

    # [ПУСТО]
    if check is None:
        for i in range(5):
            bd_set(f"INSERT INTO smeta_requirement_photo VALUES('{i + 1}', '{0}')")

    # Отправка сообщения пользователю
    text = 'Фото, которые будут отправляться пользователю при нажатии\n"Как выглядит смета?"'
    await bot.send_message(user_id, text, reply_markup=admin_smeta_requirement_photo_kb())


# Как выглядит смета - просмотр фото и редактирование
@dp.callback_query_handler(text_contains='admin_smeta_requirement_baby_photo:')
async def admin_main_kb_new_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    data = str(callback.data)

    # Проверка на наличие фото
    photo_id = data.replace("admin_smeta_requirement_baby_photo:", "")
    check = bd_get_one(f"SELECT photo FROM smeta_requirement_photo WHERE photo_id = '{photo_id}'")
    if check == '0':
        text = "Фото не загружено\n" \
               "Возможные действия:"
        await bot.send_message(user_id, text, reply_markup=admin_smeta_requirement_add_photo_kb(photo_id))

    # [Фото]
    else:
        # Фото с сжатием
        try:
            await bot.send_document(user_id, check, reply_markup=admin_smeta_requirement_change_photo_kb(photo_id))

        # Фото без сжатия
        except TypeOfFileMismatch:
            await bot.send_photo(user_id, check, reply_markup=admin_smeta_requirement_change_photo_kb(photo_id))


# Как выглядит смета - добавить фото
@dp.callback_query_handler(text_contains='admin_smeta_requirement_add_photo:')
async def admin_main_kb_new_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    photo_id = str(callback.data).replace("admin_smeta_requirement_add_photo:", "")

    bd_set(f"UPDATE user_stage SET stage_one = 'adm_set_requirement_photo:{photo_id}' WHERE user_id = '{user_id}'")
    await bot.send_message(user_id, "Отправьте фото:")


# Сохранение фото
async def admin_smeta_requirement_add_photo(message, photo_id):
    user_id = message.from_user.id
    photo_id = str(photo_id).replace("adm_set_requirement_photo:", "")

    # Фото с сжатием
    try:
        await bot.send_document(user_id, message.document.file_id)
        bd_set(f"UPDATE smeta_requirement_photo SET photo = '{message.document.file_id}' WHERE photo_id = '{photo_id}'")
        bd_set(f"UPDATE user_stage SET stage_one = '{0}' WHERE user_id = '{user_id}'")
        text = "Сообщение сохранено"
        await bot.send_message(user_id, text)

    # Фото без сжатия
    except AttributeError:
        try:
            await bot.send_photo(user_id, message.photo[-1].file_id)
            bd_set(f"UPDATE smeta_requirement_photo SET photo = '{message.photo[-1].file_id}' WHERE photo_id = '{photo_id}'")
            bd_set(f"UPDATE user_stage SET stage_one = '{0}' WHERE user_id = '{user_id}'")
            text = "Сообщение сохранено"
            await bot.send_message(user_id, text)

    # Ошибка
        except IndexError:
            await bot.send_message(user_id, "Неправильный формат, отправьте фото или документ:")


# Как выглядит смета - удалить фото
@dp.callback_query_handler(text_contains='admin_smeta_requirement_del_photo:')
async def admin_main_kb_new_q(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id
    data = str(callback.data)
    photo_id = str(data).replace("admin_smeta_requirement_del_photo:", "")

    bd_set(f"UPDATE smeta_requirement_photo SET photo = '{0}' WHERE photo_id = '{photo_id}'")
    await bot.send_message(user_id, "Фото удалено")


# Тестовый запуск
@dp.callback_query_handler(text_contains='admin_test_run')
async def admin_test_run(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    await bot.send_message(user_id, 'Здравствуйте! Это телеграм-бот smeta-spb.com\n'
                                    'Готовы ответить на ваши вопросы', reply_markup=user_ready_kb())