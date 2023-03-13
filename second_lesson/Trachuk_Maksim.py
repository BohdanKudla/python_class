import  math

print('Введите коэффициенты для квадратного уравнения')
print("a*x^2 + b*x + c = 0")
a = float(input('Коэффициент a:'))
b = float(input('Коэффициент b:'))
c = float(input('Коэффициент c:'))


D = (b ** 2) - (4 * a * c)
if D > 0:
   x1 = (-b + math.sqrt(D)) / (2 * a)
   x2 = (-b - math.sqrt(D)) / (2 * a)
   print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
elif D < 0:
    print("Нет решения")