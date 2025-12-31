import numpy as np
from numpy import random

'''
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.dtype)
print(arr1[0])
print(arr1[2:4])
for i in arr1:
    print(i)

arr2 = np.array([[1,2,3,5],[3,4,5,6]])
print(arr2.shape)
print(arr2.reshape(8,1))

arr3 = np.array([1,2,3,4,4])

arr = np.concatenate((arr1, arr3))
print(arr)

x = np.where(arr == 4)
print(x)
print(np.sort(arr))

print(random.randint(100))

print(np.arange(3)+1)

data_type = [('name', 'S15'), ('class', int), ('height', float)]

student_details = [('James', 5, 48.5), ('Naail', 6, 52.2), ('Paul', 5, 42.1), ('Pit', 5, 40.11)]

students = np.array(student_details, dtype=data_type)

print("original array")
print(students)

print("sort by height")
sorted_students = np.sort(students, order='height')
print(sorted_students)
'''


print(np.linspace(0,1,5))

print(np.zeros((2,3))) # 2x3 matrix of 0
print(np.ones((3,3))) # 3x3 matrix of 1
print(np.eye(3))  # identity matrix

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)
print(a * b)  # element wise multiplication
print(a.dot(b)) # dot product
print(np.mean(a))
print(np.std(a))  # standard deviation
print(np.sum(a))

A = np.array([[1,2], [3,4]])
print(np.linalg.inv(A))  # inverse
print(np.linalg.det(A))  # determinant
print(np.linalg.eig(A))  # eigenvalues & eigenvectors

arr = np.array([10,20,5,20,10,30,5])

print("array:", arr)
# index of max value
print(np.argmax(arr))
# index of min value
print(np.argmin(arr))
# unique values
print(np.unique(arr))