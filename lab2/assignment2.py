import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,2*np.pi)

x=np.cos(t); y=np.sin(t)

plt.plot(x,y)
plt.axis("equal")

i = 1
j = 3
n = 4

A = [np.cos(i), np.cos(j), np.cos(n), np.cos(i)]
B = [np.sin(i), np.sin(j), np.sin(n), np.sin(i)]

plt.plot(A, B, '-o')
plt.fill(A, B, '#fff313')

plt.show()