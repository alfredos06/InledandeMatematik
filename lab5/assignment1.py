import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):

    return x*np.sin(x)  

def fprime(x):

    return np.sin(x) + (x * np.cos(x))  

x = np.linspace(0, 15, 200)

plt.plot(x, f(x))

xprime0 = fsolve(fprime, 14.5)

print(f'Maxvärde {xprime0}')

plt.plot(xprime0, f(xprime0), 'o')

print(f'Maxpunkt ({xprime0}, {f(xprime0)})')

plt.show()