user_input = input("Введите последовательность чисел через пробел: ")
numbers_list = user_input.split()
int_numbers_list = []

try:
    for number in numbers_list:
        int_number = int(number)
        int_numbers_list.append(int_number)
except ValueError:
    print(f"Ошибка: некорректный ввод. Проверьте, что введены только числа, разделенные пробелами.")
    exit()

even_sum = 0

for i in range(len(int_numbers_list)):
    if i % 2 == 0:
        even_sum += int_numbers_list[i]

print(f"Сумма элементов с четными индексами: {even_sum}")


