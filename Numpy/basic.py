import numpy as np

# Checking NumPy Version 
print(np.__version__)

# Creating a array
arr = np.array([1,2,3,4,5,6])

print(arr) # Printing an array

#Print the type of array
print(type(arr))

# 0D array

arr1 = np.array(42)

print(arr1)

# 1D array

print(arr)

# 2D array

arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

# 3D array

arr3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,1,2]]])
print(arr3)

# Check Number of Dimensions

print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# Slicing 

print(arr[1:3])

# Negative Slicing

print(arr[-3:])

#Step

print(arr[1:5:2])

# Slicing 2D

print(arr2[1,1:2])

# Copy the array

x = arr.copy() # doesnot change copy array if original array value is changed

print(x)

# View

y = arr.view() # change the original and display the both array
arr[0] = 43

print(arr)
print(y)

y[0] = 42

print(arr)
print(y)

# Check if array owns its data

print(x.base) # copy
print(y.base) # view

# Shape of the array

print(arr.shape)
# if it gives (5,) it means it have only one Dimension array and contains 5 elements

# Reshaping arrays

newarr = arr.reshape(2,3)
print(newarr)

# Flattening the arrays

flat_arr = arr3.reshape(-1) # changes into 1D array

print(flat_arr)

# Iterating Arrays

for i in arr:
    print(i)


# 2D array
for i in arr2:
    print(i)


# Iterating on Each Scalar Element

for i in np.nditer(arr2):
    print(i)

# Joining the array

j_arr = np.concatenate((arr,arr2.reshape(-1)))
print(j_arr)

# 2D array

j2_arr = np.concatenate((arr2,arr2), axis=1)
print(j2_arr)

# Joining the array using Stack

s_arr = np.stack((y,arr), axis=1)
print(s_arr)

# Stack along Rows

s1_arr = np.hstack((y,arr))
print(s1_arr)

# Stack along Columns
s2_arr = np.vstack((y,arr))
print(s2_arr)

# Stack along Height (depth)

d_arr = np.dstack((y,arr))
print(d_arr)