numbers = input("Введите последовательность чисел через пробел: ")
numbers_list = numbers.split()

try:
    for number in numbers_list:
        int(number)
except ValueError:
    print("Последовательность должна состоять только из чисел")

    print(f"Сумма элементов с четными индексами: {sum(int(numbers_list[i]) for i in range(0, len(numbers_list), 2))}")