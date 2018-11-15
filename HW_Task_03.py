# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.

import sys
import random


def show_size(x, level=0, variables_sum=0):
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


# Задача №5 из домашнего задания к уроку №1.
# Пользователь вводит две буквы.
# Определить их порядковый номер в алфавите и рассчитать число букв между ними.

# l1 = ord(input('Укажите первую букву:'))                              Чтобы упростить проверку, изменил ввод.
# l2 = ord(input('Укажите вторую букву:'))
l1 = random.randint(97, 122)
l2 = random.randint(97, 122)

if l1 in range(97, 122):
    if l1 == l2:
        print('Вы указали одинаковые буквы!')
    elif l2 in range(97, 123):
        print(f'{chr(l1)} ({l1}), {chr(l2)} ({l2})\nМежду указанными буквами содержится {l2 - l1 - 1} букв.')
    else:
        print('Вы указали неверный символ!')
else:
    print('Вы указали неверный символ!')

all_variables = [l1, l2]

print(f'Всего на переменные было потрачено {show_size(all_variables)} байтов.')

# Результаты тестирования:
#
# u (117), z (122)
# Между указанными буквами содержится 4 букв.
#  type=<class 'list'>, size=44, object=[117, 122]                      <-- Эта переменная содержит перечень
# 	 type=<class 'int'>, size=14, object=117                            переменных исходного скрипта, поэтому
# 	 type=<class 'int'>, size=14, object=122                            я исключаю ее из расчетов.
# Всего на переменные было потрачено 28 байтов.

# Характеристики моей платформы:
# Windows 10 x64
# Python 3.7.0 x32
