# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

array = []

for i in range(1, 21):
    array.append(random.randint(-100, 100))

min_num = float('inf')
max_num = float('-inf')

for i in array:
    if min_num > i:
        min_num = i
    elif max_num < i:
        max_num = i

sum_of_rage = 0

for i in array:
    if min_num < i < max_num:
        sum_of_rage += i

print(array)
print(min_num, max_num)
print(sum_of_rage)
