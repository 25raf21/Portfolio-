
import numpy as np

def matrix_multiplication(matrix1, matrix2):
    return np.dot(matrix1, matrix2)

# Example
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
result = matrix_multiplication(A, B)
print("Matrix Multiplication Result:")
print(result)
