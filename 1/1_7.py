# 7. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует,
# то определить, является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('Сторона a = '))
b = int(input('Сторона b = '))
c = int(input('Сторона c = '))

if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существует.')
elif a != b and a != c and b != c:
    print('Разносторонний треугольник.')
elif a == b == c:
    print('Равносторонний треугольник.')
else:
    print('Равнобедренный треугольник.')
