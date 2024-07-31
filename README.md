### Задание №1
<pre>
1. Подключение к API и получение данных
Напишите скрипт на Python, который подключается к API и получает данные. 
Например, используйте публичное API https://jsonplaceholder.typicode.com/posts. 
Сохраните полученные данные в формате JSON в файл.
</pre>
Выполнить:

    python code_1.py

### Задание №2
<pre>
2. Обработка данных с использованием SQL
Представьте, что у вас есть таблица users в базе данных SQLite с полями id, 
name, и age. Напишите Python-скрипт, который подключается к этой базе данных, 
выбирает всех пользователей старше 30 лет и выводит их имена и возраст.
</pre>

Выполнить:

    Сначала выполнить:
    python add_db.py

    Затем выполнить:
    python code_1.py

### Задание №3
<pre>
3. Объединение данных из разных источников
Напишите скрипт на Python, который объединяет данные из двух источников. 
Первый источник - это CSV-файл с информацией о продуктах (поля: product_id, product_name). 
Второй источник - это JSON-файл с данными о продажах (поля: sale_id, product_id, amount). 
Скрипт должен объединить данные по product_id и вывести итоговую таблицу с информацией о продажах для каждого продукта.
</pre>

Выполнить:

    python code_3.py

### Задание №4
<pre>
4. Оптимизация скрипта
Дан следующий скрипт на Python для обработки списка чисел. Оптимизируйте его для повышения производительности.

Исходный скрипт
numbers = [i for i in range(1, 1000001)]
squares = []
for number in numbers:
squares.append(number ** 2)
</pre>

Выполнить:

    python code_4.py