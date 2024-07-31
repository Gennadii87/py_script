# TODO: Задание 3
"""
3. Объединение данных из разных источников
Напишите скрипт на Python, который объединяет данные из двух источников.
Первый источник - это CSV-файл с информацией о продуктах (поля: product_id, product_name).
Второй источник - это JSON-файл с данными о продажах (поля: sale_id, product_id, amount).
Скрипт должен объединить данные по product_id и вывести итоговую таблицу с информацией о продажах для каждого продукта.
"""

import pandas as pd
import json


products_csv_path = 'products.csv'

sales_json_path = 'sales.json'

products_df = pd.read_csv(products_csv_path)

with open(sales_json_path, 'r') as f:
    sales_data = json.load(f)

sales_df = pd.DataFrame(sales_data)

merged_df = pd.merge(products_df, sales_df, on='product_id', how='inner')

print(merged_df)
