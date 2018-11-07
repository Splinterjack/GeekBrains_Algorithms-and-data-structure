# Определить, какое число в массиве встречается чаще всего.

import random                                       # Создаю массив

array = []

for i in range(1, 21):
    array.append(random.randint(1, 9))

number_of_copies = 0
array_of_copies = []
num_index = 0

while num_index < len(array):                       # Создаю массив состоящий из количества повторений каждого элемента
    for num in array:                               # исходного массива.
        if array[num_index] == num:
            number_of_copies += 1
    array_of_copies.append(number_of_copies)
    number_of_copies = 0
    num_index += 1

most_often_num = 0
most_often_num_index = 0

for index, i in enumerate(array_of_copies):         # Определяю элемент исходного массива, встречающийся чаще всех.
    if i > most_often_num:
        most_often_num = i
        most_often_num_index = index


print(array)
print(array_of_copies)
print(f'Одно из самых частовстречающихся чисел:\n{array[most_often_num_index]}')
