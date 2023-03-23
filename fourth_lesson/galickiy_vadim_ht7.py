numbers = input("Введите последовательность чисел через пробел: ")
numbers_list = numbers.split()

sum_even_indexes = 0
for i in range(0, len(numbers_list), 2):
    if numbers_list[i].isdigit():
        sum_even_indexes += int(numbers_list[i])
    else:
        print("Ошибка: все элементы должны быть числами.")
        exit()

print(f"Сумма элементов с четными индексами равна: {sum_even_indexes}")
