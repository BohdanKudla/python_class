my_list = []
try:
    user = input("Введите список чисел: ")


    my_list = [int(num) for num in user.split()]







    minimum = my_list[0]

    for min_num in my_list:
        if minimum >= min_num:
            minimum = min_num


    print(f"Минимальное число {minimum}")
except ValueError:
    print("ERROR:Вы ввели не верные данные")