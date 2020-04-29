from random import randint

with open('task5.txt', "w+", encoding='utf-8') as f:
    f.write(' '.join([str(randint(1, 20)) for i in range(15)]))
    f.seek(0, 0)
    numbers = f.read().split()
    numbers = list(map(int, numbers))
    print(numbers)
    print(f'Сумма чисел: {sum(numbers)}')
