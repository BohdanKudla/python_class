# without min()
i = int(input('Add amount of cells: '))
my_list = []
try:

    for iterator in range(i):
        number = input(f"Enter a number for cell {iterator+1}: ")
        my_list.append(number)
except ValueError:
    print("Invalid input!")

for i, number in enumerate(my_list):
    print(f"Cell {i+1}: {number}")

minimum = my_list[0]

for element in my_list:
    if minimum > element:
        minimum = element

print(f'Minimum element: {minimum}')

# for pro
i = int(input('Add amount of cells: '))
my_list = []
try:

    for iterator in range(i):
        number = float(input(f"Enter a number for cell {iterator+1}: "))
        my_list.append(number)
except ValueError:
    print("Invalid input!")
print(f'Minimum element: {min(my_list)}')
