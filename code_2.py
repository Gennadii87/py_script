# TODO: Задание 2
"""
2. Обработка данных с использованием SQL
Представьте, что у вас есть таблица users в базе данных SQLite с полями id, name, и age.
Напишите Python-скрипт, который подключается к этой базе данных,
выбирает всех пользователей старше 30 лет и выводит их имена и возраст.

"""
import sqlite3


db_path = 'database.db'


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = "SELECT name, age FROM users WHERE age > 30"

cursor.execute(query)

users = cursor.fetchall()
for user in users:
    print(f"Name: {user[0]}, Age: {user[1]}")

conn.close()
