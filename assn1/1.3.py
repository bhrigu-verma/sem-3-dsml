import numpy as np

A = np.random.randint(1, 100, size=(5, 5))
B = np.random.randint(1, 100, size=(5, 5))

C = np.random.randint(1, size=(5, 5))
D = np.random.randint(1, size=(5, 5))

are_equal = np.array_equal(A,B)
print("Array A :- ", A)
print("Array B :- ", B)
print("Are A and B equal :- ", are_equal)

are_equal = np.array_equal(C, D)
print("Array C :-", C)
print("Array D:", D)
print("Are C and D equal :- ", are_equal)