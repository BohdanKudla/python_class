numbers = input("Введите последовательность чисел, разделенных пробелами: ").split()

try:
    even_sum = 0
    for ind in range(0, len(numbers), 2):
        number = int(numbers[ind])
        even_sum += number
    print(even_sum)
except ValueError:
    print(f"Пользователь, введите последовательность чисел, разделенных пробелами, а не: {' '.join(numbers)} ")
