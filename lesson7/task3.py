class Cell:
    def __init__(self, number):
        if number <= 0:
            print('Создание такой клетки невозможно')
        else:
            self.number = number

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        if self.number > other.number:
            return Cell(self.number - other.number)
        else:
            print('Операция вычитания для данных клеток невозможна')

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        if self.number >= other.number:
            return Cell(self.number // other.number)
        else:
            print('Операция деления для данных клеток невозможна')

    def make_order(self, num):
        if num <= 0:
            num = self.number
        m1 = ['*' * num for _ in range(self.number // num)]
        if self.number % num:
            m1.append('*' * (self.number % num))
        return '\n'.join(m1)


cell_1 = Cell(5)
cell_2 = Cell(3)
print(f'cell_1 = {cell_1.number}, cell_2 = {cell_2.number}')
cell_plus = cell_1 + cell_2
print(f'cell_1 + cell_2 = {cell_plus.number}')
print(cell_plus.make_order(5))
print()

cell_minus = cell_1 - cell_2
print(f'cell_1 - cell_2 = {cell_minus.number}')
print(cell_minus.make_order(4))
print()

cell_multiply = cell_1 * cell_2
print(f'cell_1 * cell_2 = {cell_multiply.number}')
print(cell_multiply.make_order(0))
print()

cell_div = cell_1 / cell_2
print(f'cell_1 / cell_2 = {cell_div.number}')
print(cell_div.make_order(1))
print()

print('Обработка операций, приводящих к клеткам с неположительным количеством ячеек:')
cell1 = Cell(-5)
cell2 = Cell(3) - Cell(8)
cell3 = Cell(3) / Cell(8)
