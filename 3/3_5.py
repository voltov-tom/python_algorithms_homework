# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random

min_int = float('inf')  # бесконечность
index = 0
array = [random.randint(-100, 100) for i in range(0, 30)]  # генерируем массив
print(array)

# print(array[array.index(min(array))], array.index(min(array)))  # однострочный вариант

for i in array:  # находим мин
    if i < min_int:
        min_int = i

for i in array:  # находим индекс
    if i == min_int:
        min_index = index
    index += 1
print(min_int, min_index)  # результат
