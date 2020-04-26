from itertools import count, cycle, islice
from random import randint, shuffle

while True:
    n = 0
    try:
        while n <= 0:
            n = int(input('Введите количество повторений: '))
        for el in islice(count(randint(1, 10)), n):
            print(el)

        print()
        arr = [chr(i) for i in range(65, 91)]
        print(arr)
        shuffle(arr)
        print(arr)
        for item in islice(cycle(arr), n):
            print(item)
        break
    except ValueError:
        print('Неверный ввод')
