numbers = input('Введите список чисел через запятую: ')

try:
    numbers_list = [float(num) for num in numbers.split(',')]
    min_number = numbers_list[0]
    for num in numbers_list:
        if num < min_number:
            min_number = num
    print(min_number)
except ValueError:
    print('Ошибка: вы ввели некорректные данные!')