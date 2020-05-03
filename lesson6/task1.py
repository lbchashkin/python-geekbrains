from time import sleep
from itertools import cycle, islice


class TrafficLight:
    __color = "red"
    red_time = 7
    yellow_time = 2
    green_time = 7

    def info(self):
        print('Текущие настройки:')
        print('Время красного сигнала:', self.red_time)
        print('Время жёлтого сигнала:', self.yellow_time)
        print('Время зелёного сигнала:', self.green_time)

    def settings(self, red=7, yellow=2, green=7):
        if type(red) == int and type(yellow) == int and type(green) == int:
            if red > yellow and green > yellow and red > 0 and yellow > 0 and green > 0:
                self.red_time = red
                self.yellow_time = yellow
                self.green_time = green
                print('Настройки были изменены')
                return
        print('Настройки не были изменены')

    def check(self, user_colors):
        colors = ['red', 'yellow', 'green', 'yellow']
        if user_colors == [] or user_colors[0] not in colors:
            return False
        iter = cycle(colors)
        while next(iter) != user_colors[0]:
            pass
        for i in range(1, len(user_colors)):
            if user_colors[i] != next(iter):
                return False
        return True

    def running(self, work=None):
        '''
        Функция запуска светофора
        Режимы работа светофора:
        1) Нет параметров / параметр - None
            Бесконечный режим
        2) Параметр - целое число
            Режим заданного количества циклов светофора
            (Цикл светофора - красный + жёлтый + зелёный сигнал светофора,
            циклы светофора отделяются между собой жёлтым сигналом светофора)
        3) Параметр - список/кортеж
            Режим работы светофора по списку/кортежу
            В списке/кортеже должен быть корректный порядок сигналов светофора
        '''
        iter = cycle([('red', self.red_time, 1), ('yellow', self.yellow_time, 3), ('green', self.green_time, 2),
                      ('yellow', self.yellow_time, 3)])
        if work is None:
            pass
        elif type(work) == int:
            if work > 0:
                iter = islice(iter, 4 * work - 1)
            else:
                print('Вы сломали светофор')
                return
        elif type(work) == list or type(work) == tuple:
            if self.check(work):
                index = ('red', 'yellow', 'green').index(work[0])
                iter = islice(iter, len(work) + index)
                for i in range(index):
                    next(iter)
            else:
                print('Неверный порядок сигналов светофора')
                return
        else:
            print('Светофор не работает в таком режиме')
            return
        for color in iter:
            self.__color = color[0]
            for i in range(color[1], 0, -1):
                print(f'\x1b[3{color[2]};4{color[2]}m \x1b[39m{i}\x1b[3{color[2]}m ', end='')
                print(f'\x1b[3{color[2]};49m -- {self.__color}', end='')
                sleep(2)
                print('\r', end='')
        print(f'\x1b[39;49m')


light = TrafficLight()
light.settings(9, 3, 9)
light.running(1)
light.running(['green', 'red'])
light.settings()
light.running(['red'])
