class ZeroDivError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b == 0:
        raise ZeroDivError('Деление на ноль!')
    else:
        print(a / b)
except ValueError:
    print('Ошибка ввода')
except ZeroDivError as error:
    print(error.txt)
