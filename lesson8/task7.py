class Complex:
    def __init__(self, a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.a, self.b = a, b
        else:
            raise ValueError('Not numbers')

    def __str__(self):
        return f'{self.a} + {self.b}*i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)


c1 = Complex(5, 5)
c2 = Complex(3, 4)
print(f'c1 = {c1}')
print(f'c1 = {c2}')
print(f'c1 + c2 = {c1 + c2}')
print(f'c1 * c2 = {c1 * c2}')
