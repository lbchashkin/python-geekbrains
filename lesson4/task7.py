def fact(n):
    factorial = 1
    for k in range(1, n + 1):
        factorial *= k
        yield factorial


while True:
    num = 0
    try:
        while num <= 0:
            num = int(input('Введите целое положительное число: '))
        i = 1
        for el in fact(num):
            print(f'{i}! = {el}')
            i += 1
        break
    except ValueError:
        print('Неверный ввод')
