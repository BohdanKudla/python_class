from typing import List, Union, Tuple


def solve_quadratic_equation(result: List, good_discriminant: float) -> Union[float, Tuple[float, float]]:
    b = result[1]

    if good_discriminant == 0:
        x = -b / (2 * result[0])
        return x
    else:
        x1 = (-b + good_discriminant ** 0.5) / (2 * result[0])
        x2 = (-b - good_discriminant ** 0.5) / (2 * result[0])
        return x1, x2


def validate_discriminant(discriminant: float) -> float:
    if discriminant < 0:
        raise Exception("Уравнение не имеет действительных корней!")
    return discriminant


def calculate_discriminant(result: List) -> float:

    discriminant = result[1] ** 2 - 4 * result[0] * result[2]
    return discriminant


def validate_user_input_list(input_list: List) -> List:
    if len(input_list) != 3:
        raise ValueError('Вы ввели не три числа!')
    try:
        result = [float(item) for item in input_list]
    except ValueError:
        raise ValueError('Введите список состоящий только из чисел!')
    if result[0] == 0 and result[1] == 0 and result[2] == 0:
        raise Exception("Уравнение имеет бесконечно много корней.")
    elif result[0] == 0:
        raise Exception("Коэффициент 'a' не может быть равен 0!")
    return result


def user_input_list() -> List:
    print("Введите три коэффициента a, b, c через пробел:")
    input_list = input().split()
    return input_list


def main():
    raw_list = user_input_list()
    good_list = validate_user_input_list(raw_list)
    raw_discriminant = calculate_discriminant(good_list)
    good_discriminant = validate_discriminant(raw_discriminant)
    quadratic_equation = solve_quadratic_equation(good_list, good_discriminant)

    print(good_discriminant)
    print(quadratic_equation)


if __name__ == '__main__':
    main()
