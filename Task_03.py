# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

massive = []                                    # Создаю случайный массив.

for i in range(1, 11):
    massive.append(random.randint(1, 100))
print(f'Исходный массив:\n{massive}\n')

max_elem = 0                                    # Получаю максимальны элемент и его индекс.
max_index = 0
for index, i in enumerate(massive):
    if i > max_elem:
        max_elem = i
        max_index = index

min_elem = 100                                  # Получаю минимальный элемент и его индекс.
min_index = 0
for index, i in enumerate(massive):
    if i < min_elem:
        min_elem = i
        min_index = index

min_elem_float = min_elem / 1                   # Создаю дубликат значения переменной.
massive[min_index] = max_elem                   # Меняю значения в массиве.
massive[max_index] = int(min_elem_float)

print(f'Минимальное и максимальное значения поменяны местами:\n{massive}')
