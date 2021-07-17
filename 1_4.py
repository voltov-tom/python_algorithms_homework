# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число, случайное вещественное число, случайный символ.
import random
import string

a = int(input('Введите целое число, диапазон от: '))
b = int(input('Введите целое число, диапазон до: '))
print(random.randint(a, b))

a = float(input('Введите целое число, диапазон от: '))
b = float(input('Введите целое число, диапазон до: '))
print(round(random.uniform(a, b), 2))

a = int(input('Введите целое число, диапазон от: '))
b = int(input('Введите целое число, диапазон до: '))
print(string.ascii_uppercase[random.randint(a, b)])
