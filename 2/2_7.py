# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
import random

equal = 1
n = random.randint(0, 100)
for i in range(2, n + 1):
    equal += i
if float(equal) == (n * (n + 1) / 2):
    print('Равенство верно.')