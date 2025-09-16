import numpy as np

b1 = np.array([[4], 
               [3], 
               [1]])

b2 = np.array([[5], 
               [2], 
               [1]])

b3 = np.array([[6], 
               [1], 
               [1]])

B = np.hstack([b1, b2, b3])

print(B)

