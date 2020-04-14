program = "Калькулятор целых чисел"
author = "Чашкин Леонид"
print(f'Программа "{program}". Автор: {author}')
name = input("Введите Ваше имя: ")
a = int(input(f'{name}, введите целое число a: '))
b = int(input(f'{name}, введите целое число b: '))
print(f'a + b = {a + b}')
print(f'a - b = {a - b}')
print(f'a * b = {a * b}')
if a == 0 and b == 0:
    degree = 'Не определено'
else:
    degree = a ** b
if b != 0:
    div = a / b
    int_div = a // b
    mod = a % b
else:
    div = 'Не определено'
    int_div = 'Не определено'
    mod = 'Не определено'
print(f'a ** b = {degree}')
print(f'a / b = {div}')
print(f'a // b = {int_div}')
print(f'a % b = {mod}')
