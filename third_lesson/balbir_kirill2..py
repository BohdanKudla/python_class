numbers_input = input("Введите список чисел, разделенных запятыми, или нажмите Enter для выхода: ")

if numbers_input:
    try:
        numbers_list = [int(number) for number in numbers_input.split(",")]
        min_number = numbers_list[0]
        for number in numbers_list:
            if number < min_number:
                min_number = number
        print(f"Минимальное число в списке: {min_number}")
    except ValueError:
        print("Введены некорректные данные. Введите список чисел, разделенных запятыми.")
