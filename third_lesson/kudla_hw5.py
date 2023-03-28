n = int(input("Введите целое неотрицательное число: ")) С функцией len
a = len(str(n))
print(a)





n = int(input("Введите целое неотрицательное число: ")) # без функции len
if n == 0:
    a = 1
else:
    a = 0
    while n > 0:
        a += 1
        n //= 10
print(a)



