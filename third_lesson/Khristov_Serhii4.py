# Feature spliting numbers
input_num = int(input('Enter the number from 10 to 99: '))
if 10 <= input_num and input_num <= 99:
    print(f'Tens:{input_num // 10}\nOnes:{input_num % 10}')
else:
    print('You wrote something wrong')