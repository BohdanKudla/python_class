#using len()
numbers = list(input('Введите список чисел: '))
print(len(numbers))

#using cycle 'for'
numbers = list(input('Введите список чисел: '))
count = 0
for item in numbers:
    count += 1
print(count)