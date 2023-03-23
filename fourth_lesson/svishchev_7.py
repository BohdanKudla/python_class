# Ввод данных
nom_list = input("Введите список чисел через пробел: ").split()
try:
    sum_num = 0
    for i in range(0, len(nom_list), 2):
        sum_num += int(nom_list[i])
    print(f"Сумма чисел с четными индексами равна: {sum_num}")
# Если ошибка ввода
except ValueError:
    print(f"Необходимо вводить только числа ")
