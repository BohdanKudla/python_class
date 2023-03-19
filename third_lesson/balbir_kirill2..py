numbers_input = input("Введите список чисел, разделенных запятыми, или нажмите Enter для выхода: ")

if numbers_input:
    try:
        numbers_list = [int(number) for number in numbers_input.split(",")]
        min_number = min(numbers_list)
        print(f"Минимальное число в списке: {min_number}")
    except ValueError:
        print("Введены некорректные данные. Введите список чисел, разделенных запятыми.")


