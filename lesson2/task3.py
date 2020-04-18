month = 0
while month <= 0 or month > 12:
    month = input('Введите номер месяца: ')
    if not month.isdigit():
        month = 0
    month = int(month)

seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for season, months in seasons.items():
    if month in months:
        print(f'Время года: {season}')
        break
# ---------------------------2 вариант (со словарём)------------------------------------------------------------
seasons = {1: 'зима', 2: 'зима', 3: 'весна',
           4: 'весна', 5: 'весна', 6: 'лето',
           7: 'лето', 8: 'лето', 9: 'осень',
           10: 'осень', 11: 'осень', 12: 'зима'
           }
print(f'Время года: {seasons[month]}')
# ---------------------------3 вариант (со списком)------------------------------------------------------------
seasons = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
print(f'Время года: {seasons[month - 1]}')
