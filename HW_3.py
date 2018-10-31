# По введенным пользователем координатам двух точек вывести уравнение прямой,
# которая проходит через эти точки.

x1 = int(input('Укажите координату x первой точки:'))
y1 = int(input('Укажите координату y первой точки:'))
x2 = int(input('Укажите координату x второй точки:'))
y2 = int(input('Укажите координату y второй точки:'))

if x1 == x2:
    print('x =', x1)
else:
    k = (y1-y2)/(x1-x2)
    b = y1 - k * x1
    print(y1, '=', k, '*', x1, '+', b)
    print(y2, '=', k, '*', x2, '+', b)

# Блок-схема:
# https://drive.google.com/file/d/1dFNlC-jsxqPWGFhvdFd4lWSg0GIscFhh/view?usp=sharing
