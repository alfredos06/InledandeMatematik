import numpy as np

A = np.array([
             [1, 4, 7, 10],
             [2, 5, 8, 11],
             [3, 6, 9, 12]
            ])

b = np.array([
             [1],
             [3],
             [5]
             ])

c = np.array([0, 2, 4, 6, 8])

print(np.shape(b))
print(np.shape(c))
print(np.max(A), np.min(A))