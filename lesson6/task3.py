class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


worker1 = Position("Иван", "Петров", "Программист Python", 80000, 30000)
print(worker1.get_full_name(), '---', worker1.position)
print(f'Общий доход: {worker1.get_total_income()}')
