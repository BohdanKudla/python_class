numbers = []

while True:
    try:
        # запрашиваем ввод пользователем
        user_input = input("Введите список чисел, разделённых пробелами: ")

        # преобразуем строку в список чисел
        numbers = [int(num) for num in user_input.split()]

        # проверяем, что в списке есть хотя бы одно число
        if not numbers:
            print("Список чисел пуст!")
            continue

        # выводим минимальное число из списка
        min_num = min(numbers)
        print("Минимальное число: ", min_num)
        break  # выходим из цикла

    except ValueError:
        print("Ошибка: в списке есть неправильное значение!")
        continue
