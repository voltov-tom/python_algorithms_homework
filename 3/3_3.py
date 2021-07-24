# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

index = 0
min_int = float('inf')  # бесконечность
max_int = float('-inf')  # -бесконечность

array = [random.randint(0, 100) for i in range(0, 10)]  # генерируем список
print(array)

# однострочный вариант
# array[array.index(max(array))], array[array.index(min(array))] = \
#     array[array.index(min(array))], array[array.index(max(array))]

for i in array:  # находим мин и мах
    if i < min_int:
        min_int = i
    elif i > max_int:
        max_int = i

for i in array:  # находим их индексы
    if i == max_int:
        max_index = index
    elif i == min_int:
        min_index = index
    index += 1

array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)
