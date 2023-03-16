# Ввод ряда чисел

try:
    list = list(map(int,input('Введите значения для списка через пробел ').split()))

# Находим минимальное значение в списке
    minimum = list[0]
    for element in list:
        if minimum >= element:
            minimum = element
# Выводим минимальное значение на экран
    print(f"Минимальное значение из списка {list}")
    print(f"min = {minimum}")

except ValueError:
    print("Повторите попытку, вводите только числа")

