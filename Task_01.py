# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

numbers = []
for i in range(2, 100):
    numbers.append(i)

divider = 2
divisible = 0

while divider <= 9:
    for i in numbers:
        if i % divider == 0:
            divisible += 1
    print(f'Divider – {divider}, divisibles – {divisible}')
    divider += 1
    divisible = 0
