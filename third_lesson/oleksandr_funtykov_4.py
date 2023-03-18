num = int(input("Введите число от 10 до 99: "))

if num < 10 or num > 99:
    print('Ошибка: вы ввели некорректные данные!')
else:
    print(f'Десятки:{num // 10}\nЕдиницы:{num % 10}')
    #tens = num // 10
    #ones = num % 10

    #print("Десятки: ", tens)
    #print("Единицы: ", ones)