# пример 1
n = int(input("Введите число: "))
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10

print("Количество цифр в числе:", count)

# пример 2
def count_digits(n):
    if n == 0:
        return 1
    else:
        return 1 + count_digits(n // 10)

n = int(input("Введите число (вариант 2): "))
count = count_digits(n)

print("Количество цифр в числе:", count)
