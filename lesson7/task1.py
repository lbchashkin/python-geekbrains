from functools import reduce


class Matrix:
    def __init__(self, matrix):
        if type(matrix) != list or not matrix or \
                not reduce(lambda x, y: x * y, [True if type(i) == list else False for i in matrix]):
            matrix = [[0]]
        n = [len(i) for i in matrix]
        max_n = max(n) if max(n) != 0 else 1
        for i in range(len(n)):
            for j in range(max_n - n[i]):
                matrix[i].append(0)
        self.matrix = matrix

    def __str__(self):
        return '\n'.join([''.join(map(lambda x: f'{x:<5}', i)) for i in self.matrix])

    def add_null_string(self, num):
        for i in range(num):
            self.matrix.append([0 for _ in range(len(self.matrix[0]))])

    def add_null_column(self, num):
        for _ in range(num):
            for j in range(len(self.matrix)):
                self.matrix[j].append(0)

    def __add__(self, other):
        n1, n2 = len(self.matrix), len(other.matrix)
        m1, m2 = len(self.matrix[0]), len(other.matrix[0])
        left_matrix = Matrix([[j for j in i] for i in self.matrix])
        right_matrix = Matrix([[j for j in i] for i in other.matrix])
        if n1 != n2:
            left_matrix.add_null_string(max(n1, n2) - n1)
            right_matrix.add_null_string(max(n1, n2) - n2)
        if m1 != m2:
            left_matrix.add_null_column(max(m1, m2) - m1)
            right_matrix.add_null_column(max(m1, m2) - m2)
        return Matrix([
            [left_matrix.matrix[i][j] + right_matrix.matrix[i][j] for j in range(len(left_matrix.matrix[i]))]
            for i in range(len(left_matrix.matrix))])


matrix1 = Matrix([[1, 2, 3], [4, 5], [6, 7], []])
print('Матрица 1:', matrix1, sep='\n')
matrix2 = Matrix([[2, 1], [2, 1]])
print('Матрица 2:', matrix2, sep='\n')
print('Матрица 1 + Матрица 2:', matrix1 + matrix2, sep='\n')
print('Матрица 2 после сложения не изменилась:')
print(matrix2)
