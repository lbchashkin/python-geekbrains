revenue = -1
costs = -1
while revenue < 0:
    revenue = int(input("Введите значение выручки: "))
while costs < 0:
    costs = int(input("Введите значение издержек: "))
if revenue > costs:
    profit = revenue - costs
    print(f'Прибыль {profit}')
    print(f'Рентабельность: {profit / revenue:.2f}')
    number = int(input("Введите количество сотрудников: "))
    print(f'Прибыль в расчёте на одного сотрудника: {profit / number:.2f}')
elif revenue == costs:
    print("Нулевая прибыль")
else:
    print(f'Убыток {costs - revenue}')
