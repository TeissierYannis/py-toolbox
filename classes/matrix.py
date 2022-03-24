import copy


class matrix:

    def __init__(self, array: list, highlight=False):
        self.matrix = []
        self.rows = len(array)
        self.columns = len(array[0])
        self.highlight = highlight

        self.matrix = copy.deepcopy(array)

    def __str__(self):

        string_to_return = ""

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.highlight:
                    if i == j:
                        string_to_return += "\033[92m" + str(round(self.matrix[i][j], 1)) + "\033[0m \t"
                    else:
                        string_to_return += "\033[93m" + str(round(self.matrix[i][j], 1)) + "\033[0m \t"
                else:
                    string_to_return += str(round(self.matrix[i][j], 1)) + " \t"
            string_to_return += "\n"

        return string_to_return

    def is_triang_sup(self):
        for i in range(len(self.matrix)):
            for j in range(i):
                if self.matrix[i][j] != 0:
                    return False
        return True

    def is_triang_inf(self):
        for i in range(len(self.matrix)):
            for j in range(i + 1, len(self.matrix)):
                if self.matrix[i][j] != 0:
                    return False
        return True

    def is_diag(self):
        if self.is_triang_sup() and self.is_triang_inf():
            return True
        return False

    def trace(self):
        sum = 0
        for i in range(len(self.matrix)):
            sum += self.matrix[i][i]
        return sum

    def is_diag_null(self):
        for i in range(len(self.matrix)):
            if self.matrix[i][i] == 0:
                return False
        return True

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other[i][j]
        return self.matrix

    def __mul__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] * other[i][j]
        return self.matrix
