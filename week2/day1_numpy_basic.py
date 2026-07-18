#Python library used for scientific computing and working with large, multi-dimensional arrays and matrices.
import numpy as np

 # creating arrays
 
 # Using list 
# arr = np.array([1,2,3,4])
#  print(arr)

# #using bulit-in-function
# zeroes = np.zeros((4,4)) # it will create a  4 by 4 arrays of 0 
# #print(zeroes)

# ones = np.ones((4,4))# a 4 by 4 arays of 1 
# #print(ones)

# range_arr = np.arange(1,10,2) # range from 1 to 9 with gap of interval 2
#  print(range_arr)

# linspace_arr = np.linspace(0,10,5)  # give 5 number btw 1 to 10 in interval of 5 
# print(linspace_arr)

## Manuplating arrays 

# arr = np.array([1,2,3,4,5,6,])
# reshape = arr.reshape((2,3))
# print(reshape)

# arr = np.array([1,2,3,4,5,6])
# expand = arr[:,np.newaxis]
# expand2 = arr[2:,np.newaxis]
# print(expand)

#Basic operation in array :

#element base opeartion
# a = np.array([1,2,3,4])
# b = np.array([4,5,6,7])
# print(a + b)  #[ 5  7  9 11]
# print(a * b)  #[ 4 10 18 28]

# Mathematical operation

# arr = np.array([2,4,6,8])
# print(np.sqrt(arr)) # [1.41421356 2.         2.44948974 2.82842712]
# print(np.mean(arr)) # 5.0
# print(np.sum(arr))  #20
# print(np.max(arr)) #8

# Array Indexing, slicing , reshaping
# arr =np.array([10,20,30,40,50,60])

# print(arr[2]) #indexing
# print(arr[2:]) #slicing
# reshape = arr.reshape((3,2))
# print(reshape)

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])

print("orignal matrx: \n",matrix)

#transpose
transpose = matrix.T
print("Transpose:\n",transpose)

another_matrix = np.array([[9,8,7],[6,5,4],[3,2,1]])
print("addition: \n",matrix + another_matrix )
