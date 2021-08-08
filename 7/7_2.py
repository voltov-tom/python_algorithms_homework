# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
from random import triangular


def merge_sort(array):
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        left_size = len(left)
        right_size = len(right)

        while i < left_size and j < right_size:
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < left_size:
            array[k] = left[i]
            i += 1
            k += 1

        while j < right_size:
            array[k] = right[j]
            j += 1
            k += 1

    return array


a = [round(triangular(0, 50), 2) for i in range(30)]
print(a)
merge_sort(a)
print(a)
