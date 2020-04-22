def degree2(x, y):
    """
    Возвращает x в степени y

    Параметры:
    x: действительное положительное число
    y: целое отрицательное число

    """
    s = 1
    for i in range(-y):
        s *= x
    return round(1 / s, 3)


a = 0
b = 0
try:
    while a <= 0:
        a = float(input('Введите действительное положительное число x: '))
    while b >= 0:
        b = int(input('Введите целое отрицательное число y: '))
    print(f'{a}^({b})')
    print('1 способ: ', end='')
    print((lambda a, b: round(a ** b, 3))(a, b))
    print('2 способ: ', end='')
    print(degree2(a, b))
except ValueError:
    print('Ошибка при вводе')
