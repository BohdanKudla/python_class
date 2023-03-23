#Пользователь вводит последовательность чисел. Программа выводит одно число -
# сумму элементов с четными индексами. Обязательны дефолтные проверки: например,
# что все введенные пользователем элементы последовательности - числа.
# Использовать инструментарий, что использовался в занятиях, без функций,
# рекурсий и так далее :)


num = input("Enter a sequence of numbers:  ")
num_list = num.split()
result_list = []

try:
    for count in num_list:
        int_count = int(count)
        result_list.append(int_count)
except ValueError:
    print("You did mistake")

sum_num = 0
for i in range(len(result_list)):
    if i % 2 == 0:
        sum_num += result_list[i]

print(f"Sum of digits with even numbers = {sum_num}")