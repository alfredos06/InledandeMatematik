import numpy as np

print('a)\n')

a = np.linspace(0, np.pi, 10)

for element in a:
    print(element)

print('\nb)\n')

b = range(2, 101, 2)

for j in b:
    print(j)


print('\nc)\n')

c = reversed(range(0, 100))

for j in c:
    if j % 2 != 0:
        print(j)

print('\nd)\n')

d = range(0, 100)

beenHere = False

for k in d:
    if k % 2 != 0:
        if beenHere == False:
            print(f'{k}')
            beenHere = True
        else:
            print(f'{k * -1}')
            beenHere = False




