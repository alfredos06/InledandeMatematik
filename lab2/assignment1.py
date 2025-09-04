import numpy as np
import matplotlib.pyplot as plt


#x=np.arange(0,4*np.pi,0.1)

x=np.linspace(0, 4*np.pi, 50, endpoint=False)

print(x)

f=np.sin(x)+0.3*np.sin(4*x)

plt.plot(x,f)
plt.show()