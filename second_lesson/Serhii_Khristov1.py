a = float(input("Add 'a' variable = "))
b = float(input("Add 'b' variable = "))
c = float(input("Add 'c' variable = "))
discriminant = (b ** 2) - (4 * a * c)
print('ax^2+bx+c = 0\n')

if discriminant > 0:
    print('X1 = ', ((-b + (discriminant ** 0.5)) / (2 * a)), '\n')
    print('X2 = ', ((-b - (discriminant ** 0.5)) / (2 * a)))
elif discriminant == 0:
    print('X = ', -b / (2 * a))
else:
    print('No Roots')
