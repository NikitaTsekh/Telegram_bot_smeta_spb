import sqlite3
import openpyxl


connect = sqlite3.connect('data_smeta.db')
cursor = connect.cursor()


# User_stage
cursor.execute("""CREATE TABLE IF NOT EXISTS user_stage(
        user_id INTEGER,
        stage_one TEXT,
        stage_two TEXT,
        stage_three TEXT
    )""")


# Фото как выглядит смета
cursor.execute("""CREATE TABLE IF NOT EXISTS smeta_photo(
        photo_id INTEGER,
        photo TEXT
    )""")


# Фото как выглядит смета
cursor.execute("""CREATE TABLE IF NOT EXISTS smeta_requirement_photo(
        photo_id INTEGER,
        photo TEXT
    )""")
