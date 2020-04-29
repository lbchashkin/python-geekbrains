def average(lst):
    return round(sum(lst) / len(lst), 3)


data = []
try:
    with open('text_3.txt', 'r', encoding='utf-8') as f:
        for line in f:
            data.append(line.split())

    staff = [info[0] for info in data if float(info[1]) < 20000]
    wage = [float(info[1]) for info in data if float(info[1]) < 20000]
    wage0 = [float(info[1]) for info in data]
    if data:
        print(f'Средняя зарплата всех сотрудников: {average(wage0)}')
        if staff:
            print('Фамилии сотрудников, получающих зарплату меньше 20000:')
            print(', '.join(staff))
            print(f'Средняя зарплата сотрудников, получающих зарплату меньше 20000: {average(wage)}')
        else:
            print('Нет сотрудников с зарплатой меньше 20000')
    else:
        print('Не найдено ни одного сотрудника в файле')
except FileNotFoundError:
    print('Файл не найден')
except IndexError:
    print('Ошибка в данных в файле')
except ValueError:
    print('Ошибка в зарплате одного из сотрудников в файле')
