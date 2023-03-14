a = 7
b = "asdasd"
c = 7.2
d = True

my_list = [5, 7, 2, 1, 99]

maximum = my_list[0]


for element in my_list:
    if maximum >= element:
        maximum = element

print(maximum)
