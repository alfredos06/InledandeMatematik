import numpy as np
def f(x): 
    return np.cos(x)-x

def Df(x): 
    return -np.sin(x)-1


x = 1
for k in range(10):
    h = -f(x)/Df(x)
    x = x + h
    print(x, h)
    if abs(h) < 1.0e-6:
        break

#om x = 0.75 behövs 3 förbättringar
#om x = 1 och 10e-6 behövs 4 förbättringar