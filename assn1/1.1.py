import numpy as np

A = np.random.randint(1, 10, size=(5, 5))

shape_of_A = A.shape

length_of_elements = A.itemsize

second_column = A[:, 1]

S = np.square(A)

reversed_A = A.flatten()[::-1]

print("Array A:\n", A)
print("Shape of the array:", shape_of_A)
print("Length of each element in bytes:", length_of_elements)
print("Elements in the second column:", second_column)
print("Array S (squared elements of A):\n", S)
print("Array elements in reverse order:", reversed_A)