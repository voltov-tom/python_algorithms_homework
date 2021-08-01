# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

a = 5
b = 6
print(f'{a} = {bin(a)}')
print(f'{b} = {bin(b)}')

print(f'{a} & {b} = {a & b} {bin(a & b)}')  # 1 "И" 0 вернет 0
print(f'{a} | {b} = {a | b} {bin(a | b)}')  # 1 "ИЛИ" 0 вернет 1
print(f'{a} ^ {b} = {a ^ b} {bin(a ^ b)}')  # 1 "искл.ИЛИ" 0 вернет 1, но вернет 1 ^ 1 вернет 0
print(f'{a} << 2 = {a << 2} {bin(a << 2)}')  # сдвиг влево 101 << 00 = 10100
print(f'{a} >> 2 = {a >> 2} {bin(a >> 2)}')  # сдвиг вправо 101 >> 1