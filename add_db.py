import sqlite3

"""
Дополнение к Заданию 2
Создаем данные для скрипта code_2

"""

db_path = 'database.db'

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
);
"""

cursor.execute(create_table_query)

users_data = [
    ('Alice', 28),
    ('Bob', 34),
    ('Charlie', 25),
    ('David', 32),
    ('Eve', 29)
]

insert_query = "INSERT INTO users (name, age) VALUES (?, ?)"

cursor.executemany(insert_query, users_data)

conn.commit()

conn.close()

print("Таблица users создана и данные добавлены.")
