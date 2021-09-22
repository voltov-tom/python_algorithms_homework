# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
import cProfile


def main():
    # вариант 1
    summ = {i: 0 for i in range(2, 10)}
    for i in range(2, 10000000):
        for j in summ:
            if i % j == 0:
                summ[j] += 1
    print(summ)

    # вариант 2
    # a = [0] * 8
    # for i in range(2, 10000000):
    #     for j in range(2, 10):
    #         if i % j == 0:
    #             a[j - 2] += 1
    # i = 0
    # while i < len(a):
    #     print(i + 2, ' - ', a[i])
    #     i += 1


cProfile.run('main()')

# вариант 1
# 6 function calls in 0.490 seconds 1m
# 6 function calls in 4.978 seconds 10m

# вариант 2
# 21 function calls in 0.719 seconds 1m
# 21 function calls in 7.229 seconds 10m
# разница в производительности видна только при больших значениях
