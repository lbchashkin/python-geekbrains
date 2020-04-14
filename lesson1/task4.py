n = 0
while n <= 0:
    n = int(input("Введите целое положительное число: "))
max = 0
while n > 0:
    if n % 10 > max:
        max = n % 10
    if max == 9:
        break
    n //= 10
print(f'Самая большая цифра в числе: {max}')
