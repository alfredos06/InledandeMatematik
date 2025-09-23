import numpy as np

d = range(0, 100)

sum = 0

beenHere = False

for k in d:
    if k % 2 != 0:
        if beenHere == False:
            sum = sum + 1 / k
            print(sum)
        else:
            sum = sum - 1 / k
            print(sum) 
        beenHere = not beenHere

sum2 = 0

for i in d:
    sum2 += ((-1)**i)/((2*i) + 1)

print('')
print(sum * 4)
print(sum2 * 4)
print(np.pi)