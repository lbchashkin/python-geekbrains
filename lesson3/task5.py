def func_sum(arr):
    s = 0
    b = True
    for i in range(len(arr)):
        if arr[i] == '#':
            b = False
            break
        try:
            s += int(arr[i])
        except ValueError:
            continue
    return s, b


total = 0
x = True
print("Вводите числа через пробел. # - завершение программы.")
while x:
    arr = input().split()
    if arr and arr[0] == "#":
        break
    arr.insert(0, total)
    total, x = func_sum(arr)
    print(f'Сумма: {total}', end=' ')
