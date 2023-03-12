import math
print('Введите цифровые значения переменных для решения уравнения ax^2 + bx + c = 0')
try:
    a = float(input('a = '))
except ValueError:
    print("Чувак, только число")
    a = float(input('a = '))
try:
    b = float(input('b = '))
except ValueError:
    print("Число это не буквы.")
    b = float(input('b = '))
try:
    c = float(input('c = '))
except ValueError:
    print("Миша, давай по новой. Только числа")
    c = float(input('c = '))

discr = b**2 - 4*a*c
print('Дискриминант D = ', discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / ( 2 * a)
    x2 = (-b - math.sqrt(discr)) / ( 2 * a)
elif discr == 0:
    x = -b / (2 * a)
    print('x', x)
elif discr < 0:
    print("Корней нет")
else:
     print('Мой мозг взорван')