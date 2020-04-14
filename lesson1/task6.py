a = 0
b = 0
while a <= 0:
    a = float(input("Введите результат спортсмена в первый день: "))
while b <= 0:
    b = float(input("Введите цель спортсмена: "))
days = 1
while a < b:
    print(f'День {days}: {a:.2f} км')
    a += 0.1 * a
    days += 1
print(f'День {days}: {a:.2f} км')
print(f'На {days}-й день спортсмен достиг результата - не менее {b:.2f} километров')
