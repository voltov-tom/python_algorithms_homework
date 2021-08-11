# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
n = int(input('Введите n: '))
summ = 0
x = 1
count = 1
while count != n:
    count = count + 1
    x = x * -0.5
    print(x)
    summ = summ + x
print(f'{summ = }')
