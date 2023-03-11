import math

a = float(input('Введите значение а: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))

discriminant = b**2-4*a*c

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print('Два корня x1=', x1, 'и x2=', x2)
elif discriminant == 0:
    x = -b / (2 * a)
    print('Один корень x=', x)
else:
    print('Нет корней')


