# 4. Определить, какое число в массиве встречается чаще всего.
import random

array = [random.randint(0, 100) for i in range(0, 30)]  # генерируем массив
most_often = {}
print(array)
for i in array:
    counter = 0
    for j in array:
        if i == j:
            counter += 1
    most_often[counter] = i
print(max(most_often.items()))
