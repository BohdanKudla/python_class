
#Способ №1
print("Введите любое неотрицательное число: ")
#Пользовательский ввод
num = input()
#Вычисляем кол-во цифр в числе

print(f"Кол-во цифр в числе {len(num)}")


#Способ №2
print("Введите любое неотрицательное число: ")
number = input()
sum = 0
for i in number:
    sum += 1

print(f"Кол-во цифр в числе {sum}")
