def int_func(s):
    s = list(s)
    s[0] = s[0].upper()
    return ''.join(s)


text = input('Введите слова, разделённые пробелом: ').split()
for i in range(len(text)):
    text[i] = int_func(text[i])
print(' '.join(text))
