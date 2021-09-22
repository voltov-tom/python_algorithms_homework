# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
import cProfile

# variant 2
# def primes(n):
#     sieve = set(range(2, n))
#     for i in range(2, int(math.sqrt(n))):
#         if i in sieve:
#             sieve -= set(range(2 * i, n, i))
#     return print(len(sieve))
from urllib3.connectionpool import xrange


# variant 1
# def primes(n):
#     print(len([x for x in range(2, n + 1) if
#                x not in [i for sub in [list(range(2 * j, n + 1, j)) for j in range(2, n // 2)] for i in sub]]))

# variant 3
def primes(n):
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
    print(len(lst))


cProfile.run('primes(9999)')

# variant 1 с генераторами просто отраватительная производительность
# 1229
# 10005 function calls in 40.258 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000   58.278   58.278 4_2.py:15(primes)
#         1    6.996    6.996   58.277   58.277 4_2.py:16(<listcomp>)
#      9998   33.262    0.003   33.262    0.003 4_2.py:17(<listcomp>)
#         1    0.000    0.000   58.278   58.278 <string>:1(<module>)
#         1    0.000    0.000   58.278   58.278 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# variant 2 множества хорошо подходят для решения таких задач
# 1229
# 7 function calls in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.003    0.003 4_2.py:31(primes)
#         1    0.000    0.000    0.003    0.003 <string>:1(<module>)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#         1    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# variant 3 средняя производительность списка
# 1229
# 1235 function calls in 2.766 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    2.766    2.766    2.766    2.766 4_2.py:21(primes)
#         1    0.000    0.000    2.766    2.766 <string>:1(<module>)
#         1    0.000    0.000    2.766    2.766 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
