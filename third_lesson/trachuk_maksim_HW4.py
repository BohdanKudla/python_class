try:
    number = int(input('Введите число: '))
    if 10 <= number <= 99:
        first = number //  10
        second = number % 10
        print(first, second)

except ValueError:
    print('Неверный ввод')
