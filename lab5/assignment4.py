import numpy as np
import matplotlib.pyplot as plt

def f(x): 
    return x**3 - np.cos(4*x)

def Df(x): 
    return (3 * (x**2)) + 4 * np.sin(4 * x)


x= np.linspace(-2, 2, 313)

plt.plot(x, f(x))

for k in [-1, -0.5, 0.5]:
    x = k
    for o in range(10):
        h = -f(x)/Df(x)
        x = x + h

        if abs(h) < 1.0e-6:
            plt.plot(x, f(x), 'o')
            print(x)
            break

plt.grid()
plt.show()
