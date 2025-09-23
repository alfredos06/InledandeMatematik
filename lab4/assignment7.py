import numpy as np
import matplotlib.pyplot as plt

TriangleX = [1, 3, 2, 1]
TriangleY = [1, 1, 3, 1]

plt.plot(TriangleX, TriangleY)


def polylen(x, y):
    L = 0
    n = len(x)
    for i in range(n -1):
        L=L+np.sqrt((x[i+1]-x[i])**2+(y[i+1]-y[i])**2)
    return L


print('Triangle')
print(polylen(TriangleX, TriangleY))

RectangleX = [1, 3, 3, 1, 1]
RectangleY = [0, 0, 2, 2, 0]

plt.plot(RectangleX, RectangleY)

print('Rectangle')
print(polylen(RectangleX, RectangleY))

plt.show()