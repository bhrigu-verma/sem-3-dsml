import numpy as np

random_array = np.random.randint(1, 500, size=(10, 10))

min_value = np.min(random_array)

max_value = np.max(random_array)

print("10x10 Array with random values:\n", random_array)
print("Minimum value in the array:", min_value)
print("Maximum value in the array:", max_value)