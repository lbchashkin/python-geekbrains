class DigitError(Exception):
    def __init__(self, txt):
        self.txt = txt


digit_list = []
s = input('Введите число: ')
while s != 'stop':
    try:
        if s.lstrip('-').isdigit() and len(s) - len(s.lstrip('-')) <= 1:
            digit_list.append(int(s))
        else:
            raise DigitError('Not digit!')
    except DigitError as error:
        print(error.txt)
    finally:
        s = input('Введите следующее число или stop для окончания ввода чисел: ')
print(digit_list)
