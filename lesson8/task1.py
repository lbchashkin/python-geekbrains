class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_digit(cls, date):
        dates = date.split('-')
        dates = list(map(int, dates))
        if cls.validation(dates[0], dates[1], dates[2]):
            return dates
        else:
            return 'Error in date'

    @staticmethod
    def validation(day, month, year):
        if day < 1 or day > 31:
            return False
        elif month < 1 or month > 12:
            return False
        elif year < 0 or year > 2020:
            return False
        else:
            return True

    def get_date(self):
        return self.__class__.date_to_digit(self.date)


d1 = Date('25-10-2019')
print(d1.get_date())
d2 = Date('20-13-2020')
print(d2.get_date())
