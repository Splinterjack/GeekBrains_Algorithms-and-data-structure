# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

import sys


def show_size(x, level=0):
    print('\t' * level, f'type={type(x)}, size={sys.getsizeof(x)}, object={x}')
    variables_sum = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
                variables_sum += sys.getsizeof(x.items)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                variables_sum += sys.getsizeof(item)
    # variables_sum += sys.getsizeof(x)
    return variables_sum


# Задача №3 из домашнего задания к уроку №1.
# По введенным пользователем координатам двух точек вывести уравнение прямой,
# которая проходит через эти точки.

# x1 = int(input('Укажите координату x первой точки:'))         Чтобы упростить проверку, изменил ввод.
# y1 = int(input('Укажите координату y первой точки:'))
# x2 = int(input('Укажите координату x второй точки:'))
# y2 = int(input('Укажите координату y второй точки:'))
x1 = 53
y1 = 23
x2 = 53
y2 = 42

if x1 == x2:
    print('x =', x1)
    all_variables = [x1, x2, y1, y2]
else:
    k = (y1-y2)/(x1-x2)
    b = y1 - k * x1
    print(y1, '=', k, '*', x1, '+', b)
    print(y2, '=', k, '*', x2, '+', b)
    all_variables = [x1, x2, y1, y2, k, b]

print(f'Всего на переменные было потрачено {show_size(all_variables)} байтов.')

# Результаты тестирования:
#
# 23 = 19.0 * 53 + -984.0
# 42 = 19.0 * 54 + -984.0
#  type=<class 'list'>, size=60, object=[53, 54, 23, 42, 19.0, -984.0]          <-- Эта переменная содержит перечень
# 	 type=<class 'int'>, size=14, object=53                                     переменных исходного скрипта, поэтому
# 	 type=<class 'int'>, size=14, object=54                                     я исключаю ее из расчетов.
# 	 type=<class 'int'>, size=14, object=23
# 	 type=<class 'int'>, size=14, object=42
# 	 type=<class 'float'>, size=16, object=19.0
# 	 type=<class 'float'>, size=16, object=-984.0
# Всего на переменные было потрачено 88 байтов.
#
# x = 53
#  type=<class 'list'>, size=52, object=[53, 53, 23, 42]
# 	 type=<class 'int'>, size=14, object=53
# 	 type=<class 'int'>, size=14, object=53
# 	 type=<class 'int'>, size=14, object=23
# 	 type=<class 'int'>, size=14, object=42
# Всего на переменные было потрачено 56 байтов.

# Характеристики моей платформы:
# Windows 10 x64
# Python 3.7.0 x32
