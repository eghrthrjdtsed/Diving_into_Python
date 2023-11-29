# class Matrix:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.data = [[0] * cols for _ in range(rows)]
#
#     def __str__(self):
#         return '\n'.join([' '.join(map(str, row)) for row in self.data])
#
#     def __repr__(self):
#         return f"Matrix(rows={self.rows}, cols={self.cols})"
#
#     def __eq__(self, other):
#         if not isinstance(other, Matrix):
#             return False
#         return self.rows == other.rows and self.cols == other.cols and self.data == other.data
#
#     def __add__(self, other):
#         if not isinstance(other, Matrix):
#             raise ValueError("Addition is only supported between two matrices.")
#         if self.rows != other.rows or self.cols != other.cols:
#             raise ValueError("Matrices must have the same dimensions for addition.")
#         result = Matrix(self.rows, self.cols)
#         result.data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
#         return result
#
#     def __mul__(self, other):
#         if not isinstance(other, Matrix):
#             raise ValueError("Multiplication is only supported between two matrices.")
#         if self.cols != other.rows:
#             raise ValueError(
#                 "Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
#         result = Matrix(self.rows, other.cols)
#         for i in range(self.rows):
#             for j in range(other.cols):
#                 result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
#         return result

