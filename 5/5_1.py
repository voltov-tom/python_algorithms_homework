# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
import collections

n = int(input('Введите количество компаний: '))

companies = collections.defaultdict()
profit_comp = collections.deque()
low_profit_comp = collections.deque()
all_profit = 0
quarter = 4

for i in range(n):
    name = input(f'Введите название {i + 1}-й компании: ')
    profit = 0
    comp = 1
    while comp <= quarter:
        try:
            profit += float(input(f'Введите прибыль за {comp}-й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        comp += 1
    companies[name] = profit
    all_profit += profit

mid_profit = all_profit / n

for i, item in companies.items():
    if item >= mid_profit:
        profit_comp.append(i)
    else:
        low_profit_comp.append(i)

print(f'Средняя прибыль для всех компаний составила: {mid_profit}')

print(f'Прибыль выше среднего у {len(profit_comp)} компаний: ')
for name in profit_comp:
    print(name, companies.get(name))

print(f'Прибыль ниже среднего у {len(low_profit_comp)} компаний: ')
for name in low_profit_comp:
    print(name, companies.get(name))
