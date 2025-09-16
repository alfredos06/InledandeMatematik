import numpy as np

A = np.array([
             [1, 4, 7, 10],
             [2, 5, 8, 11],
             [3, 6, 9, 12]
            ])

B = np.array([
    [4, 5, 6],
    [3, 2, 1],
    [1, 1, 1]
])

c = np.array ([
    [1],
    [3],
    [5]
    ])

d = np.array([0, 2, 4])

A[: ,2] = c[: , 0]
B[1, :] = d[:]
print("a)")
print(A)
print("")
print(B)

print("")
print("b)")

i = A[0, :].copy()
j = A[2, :].copy()

A[0, :] = j
A[2, :] = i

A[:, [1, 3]] = A[:, [3, 1]]

print(A)

