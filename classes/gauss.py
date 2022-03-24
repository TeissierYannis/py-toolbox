import copy

from classes.matrix import matrix


class gauss:

    def __init__(self, m1: matrix, m2: matrix):
        self.m1 = copy.deepcopy(m1)
        self.m2 = copy.deepcopy(m2)

    def __str__(self):
        string_to_return = ""
        for i in range(self.m1.columns):
            for j in range(self.m1.rows):
                if i == j:
                    string_to_return += "\033[92m" + str(round(float(self.m1.matrix[i][j]), 1)) + "\033[0m \t"
                else:
                    string_to_return += "\033[93m" + str(round(float(self.m1.matrix[i][j]), 1)) + "\033[0m \t"
            string_to_return += "\t\t\t"
            for j in range(len(self.m2.matrix[i])):
                if i == j:
                    string_to_return += "\033[92m" + str(round(float(self.m2.matrix[i][j]), 1)) + "\033[0m \t"
                else:
                    string_to_return += "\033[93m" + str(round(float(self.m2.matrix[i][j]), 1)) + "\033[0m \t"
            string_to_return += "\n"
        return string_to_return

    def clear_zeros_under_pivot(self, i):
        if self.m1.matrix[i][i] == 0:
            raise ValueError("Pivot of ma is 0")
        else:
            for j in range(i + 1, self.m1.rows):
                if self.m1.matrix[j][i] != 0:
                    self.compute(i, j)

    def clear_zeros_above_pivot(self, i):
        if self.m1.matrix[i][i] == 0:
            raise ValueError("Pivot of ma is 0")
        else:
            for j in range(i - 1, -1, -1):
                if self.m1.matrix[j][i] != 0:
                    self.compute(i, j)

    def compute(self, i, j):
        coef = self.m1.matrix[j][i] / self.m1.matrix[i][i]
        for k in range(self.m1.matrix.columns):
            self.m1.matrix[j][k] -= self.m1.matrix[i][k] * coef
            self.m2.matrix[j][k] -= (self.m2.matrix[i][k] * coef)


    def convert_to_identity(self):
        for i in range(self.m1.rows):
            for j in range(self.m1.columns):
                self.m2.matrix[i][j] = float(self.m2.matrix[i][j] / self.m1.matrix[i][i])

        for i in range(self.m1.columns):
            self.m1.matrix[i][i] = float(self.m1.matrix[i][i] / self.m1.matrix[i][i])
