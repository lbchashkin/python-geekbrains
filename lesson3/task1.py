def division(a, b):
    """Печатает результат деления a/b с обработкой ситуации деления на ноль"""
    try:
        print(f'a/b = {round(a / b, 3)}')
    except ZeroDivisionError:
        print('Нельзя поделить a/b, так как b=0. На ноль делить нельзя')


try:
    a = int(input('Введите целое число a: '))
    b = int(input('Введите целое число b: '))
    division(a, b)
except ValueError:
    print('Ошибка при вводе. Необходимо было ввести числа')
