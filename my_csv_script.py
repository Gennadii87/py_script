import csv

# Данные для CSV-файла с информацией о продуктах
products_data = [
    {"product_id": 1, "product_name": "Widget"},
    {"product_id": 2, "product_name": "Gadget"},
    {"product_id": 3, "product_name": "Thingamajig"}
]

# Путь к файлу products.csv
products_csv_path = 'products.csv'

# Запись данных в CSV-файл
with open(products_csv_path, 'w', newline='') as csvfile:
    fieldnames = ['product_id', 'product_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for product in products_data:
        writer.writerow(product)
