from admin.admin_handler import admin_smeta_add_photo, admin_smeta_requirement_add_photo
from functions import bd_get_one
from main import bot, dp, types
from user.user_handler import user_get_email, user_get_doc


# Обработчик сообщений
@dp.message_handler(content_types=['text', 'photo', 'document'])
async def send_text(message):
    user_id = message.from_user.id
    stage_one = bd_get_one(f"SELECT stage_one FROM user_stage WHERE user_id = '{user_id}'")

    # Отправка фото для сметы
    if str(stage_one).find('adm_set_photo:') > -1:
        photo_id = str(stage_one).replace('adm_set_photo:', "")
        await admin_smeta_add_photo(message, photo_id)

    # Отправка почты для что нужно для сметы
    elif str(stage_one).find('adm_set_requirement_photo:') > -1:
        photo_id = str(stage_one)
        photo_id = photo_id.replace("adm_set_requirement_photo:", "")
        await admin_smeta_requirement_add_photo(message, photo_id)

    # Пользователь отправка почты
    elif stage_one == '10':
        await user_get_email(message)

    # Пользователь отправка почты
    elif str(stage_one).find('user_send_email:') > -1:
        email = str(stage_one).replace("user_send_email:", "")
        await user_get_doc(message, email)



