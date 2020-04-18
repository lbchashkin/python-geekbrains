length = 0
while length <= 0:
    length = input('Введите количество элементов в массиве: ')
    if not length.isdigit():
        length = 0
    length = int(length)
a = []
for i in range(length):
    a.append(input(f'a[{i}] = '))
print(a)
for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)
