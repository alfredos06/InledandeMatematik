import numpy as np
import matplotlib.pyplot as plt


v0 = 10
y0 = 1.85

g = 9.82

def throwarc(x, theta):

    y = y0 - (g/((2*(v0**2)) * (np.cos(theta)**2))) * ((x - ((v0**2) * (np.sin(theta * 2)))/ (2* g))**2) + ((v0**2) * (np.sin(theta) ** 2) / (2 * g))
    return y

x = np.linspace(0, 14, 100)


plt.plot([0,14], [0, 0])
plt.plot(x, throwarc(x, np.deg2rad(45)))
plt.plot(x, throwarc(x, np.deg2rad(30)))
plt.plot(x, throwarc(x, np.deg2rad(15)))
plt.show()