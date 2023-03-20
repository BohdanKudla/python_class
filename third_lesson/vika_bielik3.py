#Алгоритм нахождения минимума в списке


print('Enter a list of numbers: ')
while True:
    try:
        list_of_number = list(map(int, input().split()))
        min_number = list_of_number[0]
        for number in list_of_number:
            if number < min_number:
                min_number = number
        print(f'Your result is: {min_number}')
        break
    except ValueError:
        print('Invalid input format,try again')
    except IndexError:
        print('You did not enter anything,try again')
