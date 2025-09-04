import numpy as np
import matplotlib.pyplot as plt
fig,ax=plt.subplots()

def f(x): 
    return ((x**2) - 1) / ((x**2) - (x**4))

ax.set_xlabel('$x$',fontsize=10)
ax.set_ylabel('$y$',fontsize=10)
ax.set_title('$y = (x^2-1)/(x^2 - x^4)$')

xa = np.linspace(-4, -0.3)
xb = np.linspace(0.3, 4)

ax.plot(xa,f(xa), color="blue", linewidth=2)
ax.plot(xb,f(xb), color="blue", linewidth=2)

ax.plot([-5, 5], [0, 0], color="red", linestyle="--")

ax.plot([0,0],[-12,5], color="red", linestyle="--")

plt.show()