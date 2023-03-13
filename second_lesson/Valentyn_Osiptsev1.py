a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))

d = (b**2) - (4*a*c)
l = 2 * a

if d == 0:
    print('Result: ' + str(-b/(2*a)))
elif d > 0:
    print('Bigger result: ' + str((-b + (d**(1/2))) / l) + ', smaller result: ' + str((-b - (d**(1/2))) / l))
else:
    print('No solution')
