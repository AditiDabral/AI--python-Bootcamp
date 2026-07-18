import numpy as np
# Brodcasting : we can do arthmetic operation in diff shape of arrays , it will expand small array 
# brodcasting and scalar 

# arr = np.array([1,2,3])
# print(arr +10) #scaling array

# matrix = np.array([[1,2,3],[4,5,6]])
# vector = np.array([1,0,1])
# print(matrix + vector )    

#output:  
#[[2 2 4]
#[5 5 7]]

#Aggregration function : summary statistics of array
#common function :

# arr = np.array([[1,2,3],[4,5,6]])
# print("sum: ",np.sum(arr))
# print("sum along rows: ",np.sum(arr, axis=1))
# print("sum along colums: ",np.sum(arr, axis=0))
# print("Max: ",np.max(arr))
# print("Min: ",np.min(arr))
# print("Standard Deviation: ",np.std(arr))
# print("Mean: ",np.mean(arr))

#Boolean indexing and filtering

arr = np.array([1,2,3,4,5,6])

even = arr[arr % 2 ==0]
print("Even: ",even)

arr[arr > 3] = 0 # condition change the value of array into 0 if its greater than 3 
print("Modified Array: ",arr)

# Random number generation

# random seeds : random numbers of fixed seeds

# np.random.seed(42)

random_array = np.random.rand(3,3)
print("Random Arrray: \n",random_array)

random_int = np.random.randint(0, 10, size=(2,3))
print("Random Integers: \n", random_int)
