import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 4 * np.pi, 0.1)

f = x * np.sin(x)

plt.plot(x, f)
plt.show()
