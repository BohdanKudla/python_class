num = int(input("Введите число от 10 до 99: "))

if num < 10 or num > 99:
    print('Ошибка: вы ввели некорректные данные!')
else:
    tens = num // 10
    ones = num % 10

    print("Десятки: ", tens)
    print("Единицы: ", ones)