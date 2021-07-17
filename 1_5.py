# 5. Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят и сколько между ними находится букв.
import string


def letter_counter(letter):
    count = 1
    for l in string.ascii_uppercase:
        if l == letter:
            return count
        else:
            count = count + 1


a = input('Input a one letter: ').upper()
b = input('Input a one letter: ').upper()

a_num = letter_counter(a)
b_num = letter_counter(b)

if a_num > b_num:
    print(f'First letter - {a_num}, second {b_num}, letters between: {a_num - b_num - 1}.')
else:
    print(f'First letter - {a_num}, second {b_num}, letters between: {b_num - a_num - 1}.')
