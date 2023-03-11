import math

print('ax^2 + bx + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

print('b^2 - 4 * a * с')
discriminant = ((b ** 2) - (4 * a * c))
print('D = ', discriminant)

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print('x1 = ', x1, 'x2 = ', x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('no roots')
