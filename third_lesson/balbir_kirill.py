n = input("Вводи числа!")
result = len(n)
print(result)



n = int(input("Вводи числа!: "))
count = 0

while n > 0:
    count += 1
    n //= 10

print("Количество цифр в числе:", count)