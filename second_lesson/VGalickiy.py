# Запрос у пользователя ввод коэффициентов
print("Введите коэффициенты для уравнения ax^2 + bx + c = 0:")
a = float(input("Введите a: "))
b = float(input("Введите b: "))
c = float(input("Введите c: "))

# Вычисление дискриминанта
D = b**2 - 4*a*c

# Проверка знака дискриминанта и вывод решения
if D > 0:
    x1 = (-b + D**0.5) / (2*a)
    x2 = (-b - D**0.5) / (2*a)
    print("Уравнение имеет два корня: x1 =", x1, "и x2 =", x2)
elif D == 0:
    x = -b / (2*a)
    print("Уравнение имеет один корень: x =", x)
else:
    print("Уравнение не имеет действительных корней")