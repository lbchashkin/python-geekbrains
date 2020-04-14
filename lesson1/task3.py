n = '0'
while int(n) <= 0:
    n = input("Введите число: ")
nn = n + n
nnn = n + n + n
print(f'{n} + {nn} + {nnn} = {int(n) + int(nn) + int(nnn)}')
