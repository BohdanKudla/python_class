#1 Первый вариант
try:

    n = int(input("Введите число: "))
    count = 0

    if n == 0:
        count = 1
    else:
        while n > 0:
            count += 1
            n //= 10
    print(f"Количество цифр в числе {count}")

except ValueError:
    print("ERROR:Вы ввели неверные данные")

#2 Второй вариант
number = input("Введите число = ")
print(len(number))