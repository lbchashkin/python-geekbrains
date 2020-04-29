def number(s):
    k = '0'
    i = 0
    while i < len(s) and s[i].isdigit():
        k += s[i]
        i += 1
    return int(k)


subjects = {}
try:
    with open('text_6.txt', 'r', encoding='utf-8') as f:
        for line in f:
            subject = line.split()
            subjects[subject[0]] = sum([number(subject[i]) for i in range(1, 4)])
    print(subjects)
except FileNotFoundError:
    print('Файл не найден')
except IndexError:
    print('Неверные данные в файле')
