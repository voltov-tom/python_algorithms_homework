# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
numbers = input('Введите последовательность чисел: ')
num = input('Введите число, которое нужно посчитать: ')
count = 0
for i in numbers:
    if i == num:
        count += 1
print(count)