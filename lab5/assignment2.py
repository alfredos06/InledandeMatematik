import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):

    return np.cos(x) - (pow(np.e, (-(x**2)/2)) * np.sin(5*x))

x = np.linspace(-2 * np.pi, 2 *  np.pi, 313)

x0 = fsolve(f, -4)

print(x0)

plt.plot(x0, f(x0), 'o')
plt.plot(x, f(x))
plt.show()