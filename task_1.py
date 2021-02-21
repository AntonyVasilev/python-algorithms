"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Companies = namedtuple('Companies', ['name', 'profit'])
companies_list = []
avg_profit = 0
less_avg = []
more_avg = []

n = int(input('Введите количество предприятий: '))

for i in range(n):
    name = input(f'Введите наименование {i + 1}-го предприятия: ')
    profit = float(input(f'Введите прибыль {i + 1}-го предприятия за 4 квартала: '))
    companies_list.append(Companies(name=name, profit=profit))
    avg_profit += profit

avg_profit /= n

for i in range(n):
    if companies_list[i].profit > avg_profit:
        more_avg.append(companies_list[i].name)
    elif companies_list[i].profit < avg_profit:
        less_avg.append(companies_list[i].name)
    # Варианта равного средней прибыли в условии нет, поэтому оставляю так.

print(f'Средняя прибыль: {round(avg_profit, 2)}')
print(f'Список компаний с прибылью больше средней: {more_avg}')
print(f'Список компаний с прибылью меньше средней: {less_avg}')

