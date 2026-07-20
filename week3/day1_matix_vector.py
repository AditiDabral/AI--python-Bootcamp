import numpy as np

a = np.array([
[1,2],
[3,4]])

b = np.array([
    [5,6],
    [7,8]
    ])

print("Addition: \n",a + b)
print("Subration: \n",b - a)

c = 2 * a
print("Scalar Multiplication: \n",c)

result = np.dot(a , b)  # multiplication of matrixes
print("Matrix multiplication \n",result)

# special matrix : 
Identity_matrix = np.eye(3)
print("Identity Matrix: \n",Identity_matrix)

zero_matrix = np.zeros((2,3))# 2 rows 3 column containng only zeroes values
print("Zero matrix: \n",zero_matrix)

Diagonal_matix = np.diag([1,2,3])
print("Diagonal Matrix: \n",Diagonal_matix)

# matrix and vector multiplication
Matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
Vector = np.array([1,0,-1])

result1 = np.dot(Matrix , Vector)
print("Matrix-Vector Multiplication: \n",result1)

print("Identity-Matrix Multiplication:\n",np.dot(Identity_matrix , Matrix))