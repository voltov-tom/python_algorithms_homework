# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Python 3.9.1 win10 x64

# Написать два алгоритма нахождения i-го по счёту простого числа.
import math
import sys

from urllib3.connectionpool import xrange


# variant 1
def primes_gen(n):
    gen = [x for x in range(2, n + 1) if
           x not in [i for sub in [list(range(2 * j, n + 1, j)) for j in range(2, n // 2)] for i in sub]]
    return print(sys.getsizeof(gen), sys.getrefcount(gen))


# variant 2
def primes_set(n):
    sieve = set(range(2, n))
    for i in range(2, int(math.sqrt(n))):
        if i in sieve:
            sieve -= set(range(2 * i, n, i))
    return print(sys.getsizeof(sieve), sys.getrefcount(sieve))


# variant 3
def primes_list(n):
    lst = []
    k = 0
    for i in xrange(2, n + 1):
        for j in xrange(2, i):
            if i % j == 0:
                k = k + 1
        if k == 0:
            lst.append(i)
        else:
            k = 0
    return print(sys.getsizeof(lst), sys.getrefcount(lst))


primes_gen(9999)
# 10008 bytes getrefcount = 2 10005 function calls in 40.258 seconds

primes_set(9999)
# 131288 bytes getrefcount = 2 7 function calls in 0.003 seconds

primes_list(9999)
# 10008 bytes getrefcount = 2 1235 function calls in 2.766 seconds

"""
Генераторное решение и списковое занимает одинаковое кол-во места т.к. используют в конечном итоге список,
решение с помощью множества занимает на порядок больше места, но самое быстрое.
Думаю, что можно использовать разные варианты решения в зависимости от машины и приоритетов.
"""
