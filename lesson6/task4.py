class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print('Машина повернула', direction)

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, "TownCar", False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, "SportCar", False)


class WorkCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, "WorkCar", False)

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, speed, color):
        super().__init__(speed, color, "PoliceCar", True)


my_work_car = WorkCar(70, 'зелёный')
police = PoliceCar(90, 'белый')
my_sport_car = SportCar(120, 'красный')
my_town_car = TownCar(50, 'серый')

print(my_work_car.name)
print('Цвет:', my_work_car.color)
my_work_car.go()
my_work_car.show_speed()
my_work_car.stop()
print()

print(my_town_car.name)
print('Цвет:', my_town_car.color)
my_town_car.go()
my_town_car.turn('налево')
my_town_car.turn('направо')
my_town_car.show_speed()
my_town_car.stop()
print()

print(police.name)
print('Полицейская машина?', police.is_police)
print('Цвет:', my_town_car.color)
police.go()
police.show_speed()
print()

print(my_sport_car.name)
print('Цвет:', my_sport_car.color)
my_sport_car.go()
my_sport_car.stop()
my_sport_car.go()
my_sport_car.show_speed()
