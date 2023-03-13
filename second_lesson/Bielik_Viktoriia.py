import math

print("Solve the quadratic equation")

a = int(input('Enter a= '))
b = int(input('Enter b= '))
c = int(input('Enter c= '))

Desc = b ** 2 - 4 * a * c

print ('Solve D  = ', Desc)
if Desc > 0:
    x1 = (-b + math.sqrt(Desc)) / (2 * a)
    x1 = (-b - math.sqrt(Desc)) / (2 * a)
elif Desc == 0:
    x = -b / (2 * a)
else:
    print('No roots')