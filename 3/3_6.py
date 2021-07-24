# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

index = 0
min_int = float('inf')  # бесконечность
max_int = float('-inf')  # -бесконечность

array = [random.randint(0, 100) for i in range(0, 10)]  # генерируем список
print(array)

for i in array:  # находим мин и мах
    if i < min_int:
        min_int = i
    elif i > max_int:
        max_int = i
print(f'min: {min_int}, max: {max_int}')

for i in array:  # находим их индексы
    if i == max_int:
        max_index = index
    elif i == min_int:
        min_index = index
    index += 1

if max_index > min_index:  # исключаем мах и мин
    b = max_index
    a = min_index + 1
else:
    a = max_index + 1
    b = min_index

equal = 0
for i in range(a, b):  # сумма элементов мужду
    equal += array[i]

print(equal)  # результат
