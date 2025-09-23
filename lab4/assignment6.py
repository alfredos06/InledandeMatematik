import numpy as np

Sn = 0

n = 0

while abs((Sn * 4) - np.pi) > (0.5 * (10**-5)):

    Sn += ((-1)**n)/((2*n) + 1)
    n += 1

print(Sn * 4)
print(n)
