import numpy as np

def matrix_operations(A, B):
    
    
    elementwise_sum = np.add(A, B)
    elementwise_product = np.multiply(A, B)
    dot_product = np.dot(A, B)
    transpose_dot_product = np.transpose(dot_product)
    
    results = {
        "elementwise_sum": elementwise_sum,
        "elementwise_product": elementwise_product,
        "dot_product": dot_product,
        "transpose_dot_product": transpose_dot_product
    }
    
    return results

A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)


results = matrix_operations(A, B)

print("\nElement-wise Sum:")
print(results['elementwise_sum'])

print("\nElement-wise Product:")
print(results['elementwise_product'])

print("\nDot Product:")
print(results['dot_product'])

print("\nTranspose of Dot Product:")
print(results['transpose_dot_product'])
