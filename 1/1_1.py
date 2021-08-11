# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
from sys import exit

a = list(input('введите трехзначное число: '))
while len(a) == 3:
    summ = int(a[0]) + int(a[1]) + int(a[2])
    mult = int(a[0]) * int(a[1]) * int(a[2])
    print(f'суммма цифр: {summ}, произведение: {mult}')
    a = list(input('введите трехзначное число: '))
else:
    exit()
