#1 Первый вариант
try:

    n = int(input("Введите число: "))
    count = 1

    while n >= 10:
        n = n // 10
        count += 1


    print(f"Количество цифр в числе {count}")

except ValueError:
    print("ERROR:Вы ввели неверные данные")

#2 Второй вариант
number = input("Введите число = ")
print(len(number))