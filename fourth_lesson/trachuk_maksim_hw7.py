# 1 вариант
numbers = input("Введите список чисел через пробел = ")
number_list = numbers.split()
index_list = []

try:
    for ele in number_list:
        index_list.append(int(ele))
except ValueError:
    print("ERROR:Не вернный ввод, проверьте наявность чисел и пробелов")

sum_index = 0
for i in range(len(index_list)):
    if i % 2 == 0:
        sum_index += index_list[i]

print(f"Сумма цифр с чётными индексами = {sum_index}")

# 2 вариант
try:
    n = input("Введите список чисел через пробел = ")
    ns_list = n.split()

    sum_index_ns = sum(map(int, ns_list[::2]))
    print(f"Сумма цифр с чётными индексами = {sum_index_ns}")
except ValueError:
    print("ERROR:Проверьте наличие чисел и пробелов в вашем вводе")
