# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random

a = [random.randint(-100, 100) for i in range(2 * int(input('Введите m для 2m+1: ')) + 1)]


def insertion_sort(array):  # сортировка вставкой
    for i in range(len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def median(array):  # находение медианы
    half = len(array) // 2
    if not len(array) % 2:
        med = (array[half - 1] + array[half]) / 2
        return med
    med = array[half]
    return med


def left_right_median(array):  # нахождение меньшего и большего плеча от медианы
    half = len(array) // 2
    insertion_sort(array)
    array_left = insertion_sort(array[:half])
    array_right = insertion_sort(array[half + 1:])
    return array_left, median(array), array_right


print(a)
print(left_right_median(a))
