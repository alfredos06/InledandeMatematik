import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def min_fun(x):
    y=x**2-np.cos(x)
    return y

z=fsolve(min_fun,1)
print(z)

x=np.linspace(-1.5,1.5)
y=min_fun(x)
plt.plot(x,y)
plt.grid('on')
plt.show()

#Nollställen +/-0.8241
