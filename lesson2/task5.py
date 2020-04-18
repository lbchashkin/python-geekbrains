my_list = [7, 5, 3, 3, 2]
print(f'Текущий рейтинг: {my_list}')
n = 0
while n <= 0:
    n = input('Введите новый элемент: ')
    if not n.isdigit():
        n = 0
    n = float(n)
k = 0
while k < len(my_list) and my_list[k] >= n:
    k += 1
my_list.insert(k, n)
print(f'Рейтинг после добавления нового элемента: {my_list}')
