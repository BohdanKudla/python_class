# Example 1
"""number = int(input("Enter the positive number: "))
counter = 0
if number == 0:
    counter = 1
    print(f"Amount of numbers: 1")
elif number > 0:
    while number > 0:
        counter += 1
        number //= 10

    print(f"Amount of numbers: {counter}")
else:
    print("You do something wrong!!!")"""
# Example 2
number = int(input("Enter the positive number: "))
counter = 0
if number == 0:
    counter = 1
    print(f"Amount of numbers: 1")
elif number > 0:
    counter = len(str(number))
    print(f"Amount of numbers: {counter}")
else:
    print("You do something wrong!!!")
