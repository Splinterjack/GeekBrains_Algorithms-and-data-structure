# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

array = []

for i in range(1, 21):
    array.append(random.randint(-100, 10))

max_of_negatives = float('-inf')
for i in array:
    if i < 0:
        if max_of_negatives < i:
            max_of_negatives = i

print(f'Наибольшее отрицательное число в массиве:\n{array}\nравняется:\n{max_of_negatives}')
