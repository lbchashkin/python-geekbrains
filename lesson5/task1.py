lines = []
i = 1
print('Введите строки. Окончание ввода - пустая строка')
while True:
    s = input(f'Введите {i} строку: ')
    i += 1
    if not s:
        break
    else:
        lines.append(s)
with open('text_1.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
