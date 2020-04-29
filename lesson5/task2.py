def words(s):
    return len(s.split())


try:
    with open("text_1.txt", "r", encoding='utf-8') as f:
        content = f.readlines()
    words_number = [words(string) for string in content]

    strings_number = len(content)

    print(f'Количество строк в файле: {strings_number}')
    for i in range(strings_number):
        print(f'Количество слов в строке {i + 1}: {words_number[i]}')
except FileNotFoundError:
    print('Файл не найден')
