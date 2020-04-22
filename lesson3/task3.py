def my_func(a, b, c):
    return sum((a, b, c)) - min((a, b, c))


try:
    a, b, c = input('Введите 3 числа через пробел: ').split()
    print(my_func(int(a), int(b), int(c)))
except ValueError:
    print('Ошибка ввода')
