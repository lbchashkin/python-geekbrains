numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
lines = []
try:
    with open('text_4.txt', 'r', encoding='utf-8') as f:
        for line in f:
            string = line.split()
            translate = numbers[string[0]]
            lines.append(line.replace(string[0], numbers[string[0]]))

    with open('results_4.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)
    print('Данные успешно записаны в новый файл')
except FileNotFoundError:
    print('Файл с данными не найден')
except KeyError:
    print('Неверные данные в файле')
except IndexError:
    print('Ошибка в данных в файле')
