import numpy as np

def solve_linear_system(A, b):
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        return "Matrix A is singular or not square, so the system cannot be solved."


A = np.array([[3, 2, -1],
              [2, -2, 4],
              [-1, 0.5, -1]])

b = np.array([1, -2, 0])

solution = solve_linear_system(A, b)

print("Solution vector x:")
print(solution)