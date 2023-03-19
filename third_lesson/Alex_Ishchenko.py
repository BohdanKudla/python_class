print("Введите Число")
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = float(input("d = "))
except ValueError:
    print('Не занимайся ерундой, пиши числа!!!!')

my_list=[a, b, c, d]
minimum = my_list [0]

for element in my_list:
    if minimum >= element:
        minimum = element
print(minimum)