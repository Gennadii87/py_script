# TODO: Задание 4
"""
4. Оптимизация скрипта
Дан следующий скрипт на Python для обработки списка чисел. Оптимизируйте его для повышения производительности.

Исходный скрипт
numbers = [i for i in range(1, 1000001)]
squares = []
for number in numbers:
squares.append(number ** 2)
"""

import time

"""Оптимизированный скрипт с использованием list comprehension"""
start = time.time()
squares = [number ** 2 for number in range(1, 1000001)]
end = time.time()

print(end-start)
