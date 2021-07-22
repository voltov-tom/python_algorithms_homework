# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.
numbers = input('Введите последовательность натуральных чисел: ')
numbers = numbers.strip().split()
length = len(numbers)
counter = {}
for i in range(length):
    count = 0
    for j in numbers[i]:
        count += int(j)
    counter[count] = numbers[i]
print(max(counter.items()))
