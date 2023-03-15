print('Пользователь, введите список из нескольких чисел, чтобы узнать минимальное из них: ')
while True:
    try:
        numbers = list(map(int, input().split()))
        min_num = numbers[0]
        for num in numbers:
            if num < min_num:
                min_num = num
        print(f'Спасибо, что воспользовались нашей программой, ваше минимальное число: {min_num}')
        break
    except ValueError:
        print('Пользователь, введите список ТОЛЬКО из ЧИСЕЛ и не оставляйте список пустым.')
    except IndexError:
        print('Пользователь, введите список ТОЛЬКО из ЧИСЕЛ и не оставляйте список пустым.')
