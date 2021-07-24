# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

min_int = float('inf')  # бесконечность

array = [random.randint(0, 100) for i in range(0, 30)]  # генерируем список
print(array)

for i in array:  # находим мин
    if i < min_int:
        min_int = i
min_int_1 = min_int
array.remove(min_int)  # удаляем мин

min_int = float('inf')

for j in array:  # находим второе мин
    if j < min_int:
        min_int = j
min_int_2 = min_int

print(min_int_1, min_int_2)  # результат
