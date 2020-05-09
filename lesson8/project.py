class Storage:
    def __init__(self, title):
        self.products = {"Принтеры": {}, "Сканеры": {}, "Ксероксы": {}}
        self.title = title

    def get_info(self):
        printers = '\n'.join(
            [f"{'-'.join(map(str, production))} --- {number}" for production, number in
             self.products['Принтеры'].items()])
        if not printers:
            printers = 'Нет принтеров'
        scanners = '\n'.join(
            [f"{'-'.join(map(str, production))} --- {number}" for production, number in
             self.products['Сканеры'].items()])
        if not scanners:
            scanners = 'Нет сканеров'
        xeroxes = '\n'.join(
            [f"{'-'.join(map(str, production))} --- {number}" for production, number in
             self.products['Ксероксы'].items()])
        if not xeroxes:
            xeroxes = 'Нет ксероксов'
        return f'На складе {self.title}:\nПринтеры:\n||Фирма-Модель-Тип||\n{printers}\n' \
               f'Сканеры:\n||Фирма-Модель-Место сканирования||\n{scanners}\n' \
               f'Ксероксы:\n||Фирма-Модель-Скорость (л/мин)||\n{xeroxes}'

    def add_products(self, production, number=1):
        types = {'Printer': 'Принтеры', 'Scanner': 'Сканеры', 'Xerox': 'Ксероксы'}
        name = types[production.__class__.__name__]
        if name == 'Принтеры':
            form = (production.firm, production.model, production.color)
        elif name == 'Сканеры':
            form = (production.firm, production.model, production.place)
        else:
            form = (production.firm, production.model, production.speed)
        if form in self.products[name].keys():
            self.products[name][form] += number
        else:
            self.products[name][form] = number

    def send_products(self, other, production, number=1):
        other.add_products(production, number)
        types = {'Printer': 'Принтеры', 'Scanner': 'Сканеры', 'Xerox': 'Ксероксы'}
        name = types[production.__class__.__name__]
        if name == 'Принтеры':
            form = (production.firm, production.model, production.color)
        elif name == 'Сканеры':
            form = (production.firm, production.model, production.place)
        else:
            form = (production.firm, production.model, production.speed)
        self.products[name][form] -= number
        if self.products[name][form] == 0:
            del self.products[name][form]


class OrgTeh:
    def __init__(self, firm, model):
        types = {'Printer': 'Принтер', 'Scanner': 'Сканер', 'Xerox': 'Ксерокс'}
        self.name = types[self.__class__.__name__]
        self.firm = firm
        self.model = model


class Printer(OrgTeh):
    def __init__(self, firm, model, color='чёрно-белый'):
        super().__init__(firm, model)
        self.color = color


class Scanner(OrgTeh):
    def __init__(self, firm, model, place='компьютер'):
        super().__init__(firm, model)
        self.place = place


class Xerox(OrgTeh):
    def __init__(self, firm, model, speed):
        super().__init__(firm, model)
        self.speed = speed


s0 = Storage('Склад')
s1 = Storage('1 отдел')
s2 = Storage('2 отдел')
s0.add_products(Printer('HP', '3656', 'цветной'), 10)
s0.add_products(Printer('HP', '3655'), 20)
s0.add_products(Scanner('HP', '5430'), 10)
s0.add_products(Scanner('HP', '5431', 'карта памяти'), 5)
s0.add_products(Scanner('HP', '5432', 'электронная почта'), 10)
s0.add_products(Xerox('HP', '4829', 10), 10)
s0.add_products(Xerox('HP', '4931', 15), 15)
print('Программа Склад оргтехники. Для выхода из программы введите stop')
k = ''
while True:
    while k != '0' and k != '1' and k != '2' and k != 'stop':
        k = input('Выберите отдел или склад (0 - Склад, 1 - 1 отдел, 2 - 2 отдел): ')
    if k == 'stop':
        break
    if k == '0':
        print('Склад')
    elif k == '1':
        print('1 отдел')
    else:
        print('2 отдел')
    n = ''
    while n != '0' and n != '1' and n != '2' and n != '3' and n != 'stop':
        n = input(
            'Выберите действие (1 - посмотреть остаток, 2 - передать оборудование, 3 - добавить оборудование, '
            '0 - выбрать другой отдел): ')
    if n == 'stop':
        break
    if n == '0':
        k = ''
        continue
    if n == '1':
        if k == '0':
            print(s0.get_info())
        elif k == '1':
            print(s1.get_info())
        else:
            print(s2.get_info())
    elif n == '3':
        n = ''
        while n != '1' and n != '2' and n != '3':
            n = input('Выберите добавляемое оборудование (1 - принтер, 2 - сканер, 3 - ксерокс, 0 - отмена): ')
        if n == '0':
            break
        f = ''
        while f == '':
            f = input('Введите фирму: ')
        m = ''
        while m == '':
            m = input('Введите модель: ')
        if n == '1':
            p = ''
            while p != '1' and p != '2':
                p = input('Выберите тип принтера (1 - чёрно-белый, 2 - цветной): ')
            p = {'1': 'чёрно-белый', '2': 'цветной'}[p]
            my_class = Printer(f, m, p)
        elif n == '2':
            p = ''
            while p != '1' and p != '2' and p != '3':
                p = input('Выберите место сканирования (1 - компьютер, 2 - карта памяти, 3 - электронная почта): ')
            p = {'1': 'компьютер', '2': 'карта памяти', '3': 'электронная почта'}[p]
            my_class = Scanner(f, m, p)
        else:
            p = 0
            while p <= 0:
                try:
                    p = int(input('Введите скорость копирования: '))
                except ValueError:
                    p = 0
            my_class = Xerox(f, m, p)
        n = 0
        while n <= 0:
            try:
                n = int(input('Введите количество: '))
            except ValueError:
                n = 0
        if k == '0':
            s0.add_products(my_class, n)
        elif k == '1':
            s1.add_products(my_class, n)
        else:
            s2.add_products(my_class, n)
    else:
        k1 = ''
        lst = ['1', '2', '3', '0', 'stop']
        lst.remove(k)
        while k1 not in lst:
            k1 = input('Выберите кому нужно отправить оборудование (0 - Склад, 1 - 1 отдел, 2 - 2 отдел, 3 - отмена): ')
        if k1 == 'stop':
            break
        if k1 == '3':
            continue
        FROM = {'0': s0, '1': s1, '2': s2}[k]
        TO = {'0': s0, '1': s1, '2': s2}[k1]
        n = ''
        while n not in ['1', '2', '3']:
            n = input('Выберите передаваемое оборудование (1 - принтер, 2 - сканер, 3 - ксерокс): ')
        if n == '1':
            if not FROM.products['Принтеры']:
                print('Нет принтеров для передачи!')
            else:
                prod = FROM.products['Принтеры']
                n = 0
                while n not in range(1, len(prod) + 1):
                    i = 0
                    for product in prod.keys():
                        print(f'{i + 1} {"-".join(map(str, product))}')
                        i += 1
                    try:
                        n = int(input('Выберите номер передаваемого оборудования: '))
                    except ValueError:
                        n = 0
                n = list(prod.keys())[n - 1]
                num = 0
                while num not in range(1, prod[n] + 1):
                    try:
                        num = int(input(f'Введите количество (максимум - {prod[n]}): '))
                    except ValueError:
                        num = 0
                FROM.send_products(TO, Printer(n[0], n[1], n[2]), num)
                print('Передача произошла успешно')
        elif n == '2':
            if not FROM.products['Сканеры']:
                print('Нет сканеров для передачи!')
            else:
                prod = FROM.products['Сканеры']
                n = 0
                while n not in range(1, len(prod) + 1):
                    i = 0
                    for product in prod.keys():
                        print(f'{i + 1} {"-".join(map(str, product))}')
                        i += 1
                    try:
                        n = int(input('Выберите номер передаваемого оборудования: '))
                    except ValueError:
                        n = 0
                n = list(prod.keys())[n - 1]
                num = 0
                while num not in range(1, prod[n] + 1):
                    try:
                        num = int(input(f'Введите количество (максимум - {prod[n]}): '))
                    except ValueError:
                        num = 0
                FROM.send_products(TO, Scanner(n[0], n[1], n[2]), num)
                print('Передача произошла успешно')
        else:
            if not FROM.products['Ксероксы']:
                print('Нет ксероксов для передачи!')
            else:
                prod = FROM.products['Ксероксы']
                n = 0
                while n not in range(1, len(prod) + 1):
                    i = 0
                    for product in prod.keys():
                        print(f'{i + 1} {"-".join(map(str, product))}')
                        i += 1
                    try:
                        n = int(input('Выберите номер передаваемого оборудования: '))
                    except ValueError:
                        n = 0
                n = list(prod.keys())[n - 1]
                num = 0
                while num not in range(1, prod[n] + 1):
                    try:
                        num = int(input(f'Введите количество (максимум - {prod[n]}): '))
                    except ValueError:
                        num = 0
                FROM.send_products(TO, Xerox(n[0], n[1], n[2]), num)
                print('Передача произошла успешно')
