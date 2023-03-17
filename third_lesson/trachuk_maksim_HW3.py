my_list = []
num = int(input("Какое количество чисел вы хотите? "))



for ele in range(num):

    try:
        number = int(input("Введите число ="))
        my_list.append(number)

    except ValueError:
        print("ERROR: Вы ввели не число. Попробуйте еще раз")



minimum = my_list[0]

for min_num in my_list:
        if minimum >= min_num:
            minimum = min_num

print(f"Минимальное число {minimum}")
