from sys import argv


def wage(hours, rate, premium):
    return hours * rate + premium


try:
    _, arg1, arg2, arg3 = argv
    print(wage(int(arg1), int(arg2), int(arg3)))
except ValueError:
    print('Ошибка при вводе')
