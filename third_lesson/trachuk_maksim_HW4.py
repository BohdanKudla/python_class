try:
    number = int(input('Введите число: '))
    if 10 <= number <= 99:
        print(number // 10, number % 10)
    else:
        print('Неверный ввод')
except ValueError:
    print('Неверный ввод')