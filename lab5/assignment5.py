import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fminbound

def f(x):
    return  ((1 + x**2) - (1.5 * x**3) + (0.5 * x**4)) / (1 + x**4)

def h(x): 
    return -f(x)

x = np.linspace(-3, 3, 313)

plt.plot(x, f(x))

xmin = fminbound(f, 1, 2)
xlocalmin = fminbound(f, -0.1, 0.1)

xmax = fminbound(h, -2, -1)
xlocalmax = fminbound(h, 0, 1)


plt.plot(xmin, f(xmin), 'o')
plt.plot(xmax, f(xmax), 'o')
plt.plot(xlocalmin, f(xlocalmin), 'o')
plt.plot(xlocalmax, f(xlocalmax), 'o')

plt.text(xmin, f(xmin) + 0.1, f'({round(xmin, 2)}, {round(f(xmin), 2)}): Min')
plt.text(xmax, f(xmax) + 0.1, f'({round(xmax, 2)}, {round(f(xmax), 2)}): Max')

plt.text(xlocalmax, f(xlocalmax) + 0.1, f'({round(xlocalmax, 2)}, {round(f(xlocalmax), 2)}): Local Max')
plt.text(xlocalmin - 2, f(xlocalmin) - 0.1, f'({round(xlocalmin, 2)}, {round(f(xlocalmin), 2)}): Local Min')


plt.grid()
plt.show()
