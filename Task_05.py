# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.

start_symbol = 32
end_symbol = 127
symbol = 32

while symbol <= 127:
    if symbol % 10 == 1:
        print(f'{symbol:>4} – {chr(symbol):>1}')
    else:
        print(f'{symbol:>4} – {chr(symbol):>1}', end='  ')
    symbol += 1