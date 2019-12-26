'''
1)	Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

'''


class Matrix:
    row, col, count, enter  = 0, 0, 0, 0

    def __init__(self, matrix):
        self.matrix = matrix
        #Matrix.__str__(self)

    def __str__(self):
        Matrix.count += 1
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[r])):
                print(self.matrix[r][c], end=' ')
            print()
        print(f' {"-"*10} end Matrix_{Matrix.count}')
        return ('-'*10)

    def __add__(self, other):
        print('Сумма = ')
        M_res = [[self.matrix[r][c] + other.matrix[r][c] for c in range(len(self.matrix[r]))] for r in range(len(self.matrix))]
        return Matrix(M_res)


def enter_matrix():
    Matrix.enter += 1
    try:
        if Matrix.enter == 1:
            Matrix.row = int(input(f'Кол-во строк Матрицы_{Matrix.enter}? = '))
            Matrix.col = int(input(f'Кол-во столбцов Матрицы_{Matrix.enter}? = '))
        elif Matrix.enter > 1:
            print(f'Кол-во строк Матрицы_{Matrix.enter}? = ', Matrix.row)
            print(f'Кол-во столбцов Матрицы_{Matrix.enter}? = ', Matrix.col)

        row = Matrix.row
        col = Matrix.col
        if row == col == 0:
            print('Сумма = ', 0)
            quit()
        else:
            matrix = [[int(input(f'Введите элемент матрицы [{r + 1}]стр.[{c + 1}]стлб: ')) for c in range(col)] for r in range(row)]
            return matrix
    except ValueError:
        print('Только числа! ')
        quit()





m1 = Matrix(enter_matrix())
m2 = Matrix(enter_matrix())
#m3 = Matrix(enter_matrix())
m1.__str__()
m2.__str__()
#m3.__str__()
print(m1 + m2)
#print(m1 + m2 + m3)

