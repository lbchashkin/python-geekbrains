class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        super().__init__("Pen")

    def draw(self):
        print('Запуск рисования ручкой')


class Pencil(Stationery):
    def __init__(self):
        super().__init__("Pencil")

    def draw(self):
        print('Запуск рисования карандашом')


class Handle(Stationery):
    def __init__(self):
        super().__init__("Handle")

    def draw(self):
        print('Запуск рисования маркером')


stationery1 = Stationery('my_stationery')
print('Метод рисования в родительском классе:')
stationery1.draw()
print()

my_pen = Pen()
print(f'Название канцелярской принадлежности: {my_pen.title}')
print('Вызов метода рисования:')
my_pen.draw()
print()

my_pencil = Pencil()
print(f'Название канцелярской принадлежности: {my_pencil.title}')
print('Вызов метода рисования:')
my_pencil.draw()
print()

my_handle = Handle()
print(f'Название канцелярской принадлежности: {my_handle.title}')
print('Вызов метода рисования:')
my_handle.draw()
