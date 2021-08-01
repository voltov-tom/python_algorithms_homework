# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
import string

print(string.ascii_uppercase[int(input('Input a number of letter: ').upper()) - 1])
