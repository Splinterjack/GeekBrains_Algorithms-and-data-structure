# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

import sys
import random


def show_size(x, level=0, variables_sum=0):
    variables_sum += sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                variables_sum += sys.getsizeof(item)
                show_size(item, level + 1)
    return variables_sum

# Задача №3 из домашнего задания к уроку №3.
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


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

print(f"Минимальное и максимальное значения поменяны местами:\n{massive}\n")
print(f'Всего на переменные было потрачено {show_size(massive) + show_size(max_elem) + show_size(max_index)} байтов.')

# Результаты тестирования:
#
# Исходный массив:
# [75, 22, 91, 84, 9, 31, 89, 2, 80, 68]
#
# Минимальное и максимальное значения поменяны местами:
# [75, 22, 2, 84, 9, 31, 89, 91, 80, 68]
#
#  type=<class 'list'>, size=100, object=[75, 22, 2, 84, 9, 31, 89, 91, 80, 68]
# 	 type=<class 'int'>, size=14, object=75
# 	 type=<class 'int'>, size=14, object=22
# 	 type=<class 'int'>, size=14, object=2
# 	 type=<class 'int'>, size=14, object=84
# 	 type=<class 'int'>, size=14, object=9
# 	 type=<class 'int'>, size=14, object=31
# 	 type=<class 'int'>, size=14, object=89
# 	 type=<class 'int'>, size=14, object=91
# 	 type=<class 'int'>, size=14, object=80
# 	 type=<class 'int'>, size=14, object=68
#  type=<class 'int'>, size=14, object=91
#  type=<class 'int'>, size=14, object=2
# Всего на переменные было потрачено 268 байтов.

# Характеристики моей платформы:
# Windows 10 x64
# Python 3.7.0 x32
