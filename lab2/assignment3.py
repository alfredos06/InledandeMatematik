import numpy as np
import matplotlib.pyplot as plt

t=np.linspace(0,2*np.pi)

plt.title("Title")

plt.subplot(121)

x = np.cos(t) + np.cos(3 * t)
y = np.sin(2 * t)

plt.plot(x, y)
plt.axis("equal")

plt.subplot(122)

x = np.cos(t) + np.cos(4 * t)
y = np.sin(2 * t)

plt.plot(x, y)
plt.axis("equal")
plt.show()