# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
from string import ascii_letters


def search_substring(s):
    n = len(s)
    arr_string = set()
    for i in range(1, n):
        for j in range(n - i + 1):
            k = hash(s[j:j + i])
            if k not in arr_string:
                arr_string.add(k)
    return len(arr_string)


def validate(s):  # проверка на латинские символы
    return all(map(lambda c: c in ascii_letters, s))


while True:
    string = input('Введите строку состоящую только из латинских букв: ').lower()
    if validate(string):
        print(f'Количество подстрок: {search_substring(string)}')
        break
