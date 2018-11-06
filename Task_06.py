# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше загаданного введенное пользователем число.
# Если за 10 попыток число не отгадано, то вывести его.

import random

number = random.randint(0,100)

print(number)
my_try = 1
print(f'Попытка № {my_try}.')
assumption = int(input('Угадайте загаданное число:'))

while True:
    my_try += 1
    if my_try == 11:
        print(f'Вы исчерпали попытки.\nБыло загадано число {number}')
        break
    elif assumption == number:
        print(f'Поздравляем! Вы угадали!\nБыло загаданно число {number}.')
        break
    elif number < assumption:
        print('Загаданное число – меньше.')
    else:
        print('Загаданное число – больше.')
    assumption = int(input(f'Попытка № {my_try}:'))


