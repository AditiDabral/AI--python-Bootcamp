# determinants : scalar value that provoide info about a matrix's properties
#only for square matrix , det(A) = 0 (the matrix A is singular) , det(A) != 0 (A is invertible)

# det([a , b],[c , d])= ad - cd

import numpy as np

A = np.array([[2, 3],[1, 4]])
determinant = np.linalg.det(A)  #linalg : linear algebra
print("Determinant of 2X2 Matrix: \n", determinant)

# inverse matix : A^-1 , A * A^-1 = I , Matrix is invertible only if det(A) != 0 
inverse = np.linalg.inv(A)
print("Inverse of A: \n",inverse)

# eigen values  and eigen vector 
# Av = λv
# where:

# A = the matrix (the transformation)
# v = the eigenvector
# λ (lambda) = the eigenvalue

# A = [[2,0],[0,3]]
# v1 = [[1],[0]]

# multiply Av1 = [[2],[0]] = 2v1
# Eigenvector = (1,0)
# Eigenvalue = 2

#eigenvector points in the direction where the matrix transformation stretches or commpresses vector
#Eigenvalues : indicate the factor of stretching or compression , they can be real or complex , [ for symmetric matrix eigen =values are always real]

eigenValues , eigenVectors = np.linalg.eig(A)
print("Eigen val\n",eigenValues)
print("Eigenvector \n",eigenVectors)

B = np.array([[4,2],[1,1]])
eigval , eigvec = np.linalg.eig(B)
print("EigenValue",eigval)
print("Eigenvector:\n",eigvec)

# Matrix decompostion : process of breaking a matix into simpler componenets to analyze or solve problem\
# Singular Value Decomposition (SVD) : it decompose a matrix A into 3 matrices A = UΣVᵀ

# where:

# A = the original matrix
# U = tells us the final directions of the transformed data.[left singular vectors] (orthogonal matrix )
# Σ (Sigma) = tells us how much stretching or shrinking happens.[Diagonal matrix of singular values] (non negative)
# Vᵀ = tells us the original directions in the data. [ right singular vectors ](orthogonal matrix)

# application SVD : image compressin, noise reduction

U, S, Vt = np.linalg.svd(A)
print("U: \n",U)
print("S: \n",S)
print("V transpose: \n",Vt)

import numpy as np

# Original matrix (3 x 2)
C = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("Original Matrix:\n", C)

# Perform SVD
U1, S1, Vt1 = np.linalg.svd(C, full_matrices=False)

# Create Sigma matrix from singular values
Sigma1 = np.diag(S1)

# Reconstruct the original matrix
reconstructed1 = U1 @ Sigma1 @ Vt1

print("\nU Matrix:\n", U1)
print("\nSingular Values (S):\n", S1)
print("\nSigma Matrix:\n", Sigma1)
print("\nVt Matrix:\n", Vt1)
print("\nReconstructed Matrix:\n", reconstructed1)

# Check the shapes
print("\nShapes:")
print("U:", U1.shape)
print("Sigma:", Sigma1.shape)
print("Vt:", Vt1.shape)