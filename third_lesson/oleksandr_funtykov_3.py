numbers = input('Введите список чисел через запятую: ')

try:
    numbers_list = [float(num) for num in numbers.split(',')]
    min_number = min(numbers_list)
    print(f'Минимальное число: {min_number}')
except ValueError:
    print('Ошибка: вы ввели некорректные данные!')
