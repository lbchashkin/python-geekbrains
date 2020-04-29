from json import dump

firms = [{}]
try:
    with open('text_7.txt', 'r', encoding='utf-8') as f:
        for line in f:
            data = line.split()
            firms[0][data[0]] = int(data[2]) - int(data[3])
    average_profit = [profit for profit in firms[0].values() if profit > 0]
    if average_profit:
        firms.append({'average_profit': round(sum(average_profit) / len(average_profit), 3)})
        with open('text_777.json', 'w', encoding='utf-8') as f:
            dump(firms, f, ensure_ascii=False, indent=4)
        print('Данные успешно записаны в новый файл')
    else:
        print('Нет фирм с прибылью')
except FileNotFoundError:
    print('Файл не найден')
except IndexError:
    print('Ошибка в данных в файле')
except ValueError:
    print('Неверные данные в файле')
