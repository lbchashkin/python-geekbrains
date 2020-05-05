from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title, param):
        self.title = title
        self.param = param

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    @property
    def calculation(self):
        return round(self.param / 6.5 + 0.5, 2)


class Costume(Clothes):
    @property
    def calculation(self):
        return round(2 * self.param + 0.3, 2)


new_coat = Coat('Пальто женское', 100)
new_costume = Costume('Костюм мужской', 70)
print(f'Расход ткани для {new_coat.title}:', new_coat.calculation)
print(f'Расход ткани для {new_costume.title}:', new_costume.calculation)
