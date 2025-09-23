
x1 = 6

a = (x1 > 5 or x1 < -1)

print('')
print(f'a) Är värdet x1 = {x1} inte inom intervallet [-1, 5]: {a}\n')

x2 = 1
y2 = -3

b = ((x2 >= 0 and x2 <= 1) or (y2 >= -4 and y2 <= 4))

print(f'b) Är värdet x2 = {x2} inom intervallet [0, 1] eller är värdet y2 = {y2} inom intervallet [-4, 4]: {b}\n')

x3 = -1
y3 = 1

c = ((x3**2) + (y3**2) <= 1)

print(f'Is the point ({x3}, {y3}) inside of a circle with a radius of 1 with a midpoint in (0, 0): {c}')
