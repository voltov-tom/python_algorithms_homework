# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления
# программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
import sys

while True:
    numbers = input('Введите числа и операцию: ')
    if numbers == '0':
        sys.exit()
    elif numbers.find('+') != -1:
        numbers = numbers.strip().split('+')
        print(float(numbers[0]) + float(numbers[1]))
    elif numbers.find('-') != -1:
        numbers = numbers.strip().split('-')
        print(float(numbers[0]) - float(numbers[1]))
    elif numbers.find('*') != -1:
        numbers = numbers.strip().split('*')
        print(float(numbers[0]) * float(numbers[1]))
    elif numbers.find('/') != -1:
        numbers = numbers.strip().split('/')
        if float(numbers[1]) == 0:
            print('ZeroDivisionError')
        else:
            print(float(numbers[0]) / float(numbers[1]))
    else:
        print('Неверный ввод, начните заного')
