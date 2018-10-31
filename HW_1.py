# Найти сумму и произведение цифр введённого пользователем трехзначного числа.

a = int(input("Введите челое трехзначное число: "))
my_sum = (a // 100) + (a % 100 // 10) + (a % 10)
product = (a // 100) * (a % 100 // 10) * (a % 10)
print(my_sum)
print(product)

# Блок-схема:
# https://drive.google.com/file/d/1dFNlC-jsxqPWGFhvdFd4lWSg0GIscFhh/view?usp=sharing