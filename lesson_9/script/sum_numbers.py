"""
 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
    6782 -> 23
    0,56 -> 11
"""


def sum_numbers(numbers: str):
    result_sum = 0
    for number in numbers:
        if number.isdigit():
            result_sum += int(number)
    return result_sum


def main():
    user_send = input('Ведите любое число с любыми символами: ')
    print(sum_numbers(user_send))


if __name__ == "__main__":
    main()
