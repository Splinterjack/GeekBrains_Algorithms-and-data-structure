# Выполнить логические побитовые операции "И", "ИЛИ" и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

a = 5     # 0b101
b = 6     # 0b110
print('binary "a" =', bin(a))
print('binary "b" =', bin(b))
print("a AND b =", a & b, bin(a & b))
print("a OR b =", a | b, bin(a | b))
print("a XOR b =", a ^ b, bin(a ^ b))
print("NOT a =", ~ a, bin(~ a))
print("a >> 2 =", a >> 2, bin(a >> 2))
print("a << 2 =", a << 2, bin(a << 2))

# Блок-схема:
# https://drive.google.com/file/d/1dFNlC-jsxqPWGFhvdFd4lWSg0GIscFhh/view?usp=sharing