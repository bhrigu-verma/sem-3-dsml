import numpy as np

def statistical_operations(M):
    mean_of_rows = np.mean(M, axis=1)
    std_of_columns = np.std(M, axis=0)
    variance_of_matrix = np.var(M)
    median_of_matrix = np.median(M)
    
    results = {
        "mean_of_rows": mean_of_rows,
        "std_of_columns": std_of_columns,
        "variance_of_matrix": variance_of_matrix,
        "median_of_matrix": median_of_matrix
    }
    
    return results
    
M = np.array([
    [4, 8, 15, 16],
    [23, 42, 9, 7],
    [5, 12, 19, 21]
])

results = statistical_operations(M)

print("Matrix M:")
print(M)

print("\nMean of each row:")
print(results['mean_of_rows'])

print("\nStandard deviation of each column:")
print(results['std_of_columns'])

print("\nVariance of the entire matrix:")
print(results['variance_of_matrix'])

print("\nMedian of the entire matrix:")
print(results['median_of_matrix'])
