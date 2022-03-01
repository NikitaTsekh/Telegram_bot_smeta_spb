import openpyxl
from openpyxl.styles import Font

from data.data import cursor
from functions import bd_set, get_date, get_time, bd_get_many, bd_get_one
from main import bot, dp, types

cursor.execute("""CREATE TABLE IF NOT EXISTS admin_user_stat(
        user_id INTEGER,
        date TEXT,
        time Text
    )""")


# trigger
# Записывает информацию о срабатывании в admin_user_stat
def admin_stat_trigger(user_id):
    bd_set(f"INSERT INTO admin_user_stat VALUES('{user_id}', '{get_date()}', '{get_time()}')")


# Сохранение результатов в excel
def admin_stat_to_excel():

    # Создаем книгу
    book = openpyxl.Workbook()

    # Создаём первую страницу "По дням"
    sheet = book.active
    sheet.title = 'По дням'

    # Блок с датой составления отчёта
    sheet.row_dimensions[1].height = 50
    sheet.row_dimensions[2].height = 50
    sheet["A1"] = "Дата составления отчёта:"
    sheet["A1"].font = Font(bold=True)
    sheet["B1"] = str(get_date())
    sheet["B1"].font = Font(bold=True)

    # Создаём заголовки столбцов
    sheet["A2"] = "Дата"
    sheet.column_dimensions["A"].width = 30
    sheet["A2"].font = Font(bold=True)

    sheet["B2"] = "Число уникальных пользователей"
    sheet.column_dimensions["B"].width = 40
    sheet["B2"].font = Font(bold=True)

    row = 3
    # Выбираем уникальные дни из базы данных
    days = bd_get_many(f"SELECT DISTINCT date FROM admin_user_stat")

    # Заполняем таблицу
    for day in days:
        try:
            # Менеджер по продажам
            sheet[row][0].value = day

            # Время
            users = bd_get_many(f"SELECT DISTINCT user_id FROM admin_user_stat WHERE date = '{day}'")
            users = len(users)
            sheet[row][1].value = users

            row += 1
        except Exception as e:
            print(e)

    # Создаём вторую страницу "По месяцам"
    sheet = book.create_sheet("По месяцам")
    sheet.row_dimensions[1].height = 50

    sheet["A1"] = "Месяц и год"
    sheet.column_dimensions["A"].width = 30
    sheet["A1"].font = Font(bold=True)

    sheet["B1"] = "Уникальных пользователей"
    sheet.column_dimensions["B"].width = 30
    sheet["B1"].font = Font(bold=True)

    row = 2

    # Словарь месяцов c уникальными пользователями
    month = {}
    days = bd_get_many(f"SELECT date FROM admin_user_stat")
    for day in days:
        day_month = day[3::]
        if day_month not in month:
            users = bd_get_many(f"SELECT DISTINCT user_id FROM admin_user_stat"
                                f" WHERE date LIKE '%{day_month}'")
            month[day_month] = len(users)

    # Теперь в словаре month находятся месяц, год и число уникальных пользователей
    try:
        for day_month in month:
            # Месяц и год
            date = day_month
            sheet[row][0].value = date

            # Число пользователей
            sheet[row][1].value = month[day_month]

            row += 1

    except Exception as e:
        print(e)

    # Сохраняем таблицу
    book.save("stat.xlsx")
    book.close()


# admin_get_stat
# Отправка статистики
@dp.callback_query_handler(text_contains='admin_get_stat')
async def admin_get_stat(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    user_id = callback.from_user.id

    caption = f"Статистика от {get_date()}"
    admin_stat_to_excel()
    doc = open(r'stat.xlsx', 'rb')
    await bot.send_document(user_id, doc, caption=caption)
