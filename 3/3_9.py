# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

matrix = []
num_of_columns = int(input('Введите количество столбцов матрицы: '))
num_of_lines = int(input('Введите количество строк матрицы: '))

for j in range(num_of_lines):
    matrix.append([random.randint(0, 100) for i in range(num_of_columns)])

for i in matrix:
    print(i)

min_int = float('inf')  # бесконечность
max_int = float('-inf')  # -бесконечность

for j in range(num_of_columns):
    for i in range(num_of_lines):
        if matrix[i][j] < min_int:
            min_int = matrix[i][j]
    if min_int > max_int:
        max_int = min_int

print(max_int)
