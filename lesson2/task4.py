string = input('Введите слова: ')
for number, s in enumerate(string.split(), 1):
    if len(s) > 10:
        s = s[:10]
    print(f'{number}: {s}')
