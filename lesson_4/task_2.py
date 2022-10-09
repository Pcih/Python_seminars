"""
Task_2
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
70 = 2*5*7 => [2, 5, 7]
140 = 2*2*5*7 => [2, 2, 5, 7]
140|2
 70|2
 35|5
  7|7
"""

# prime_numbers = [2, 3, 5, 7]


def get_mult(user_send: int):

    prime_number = 2
    lst = []
    while prime_number <= user_send:
        if user_send % prime_number == 0:
            lst.append(prime_number)
            user_send //= prime_number
            prime_number = 2
        else:
            prime_number += 1
    return lst


def main():
    print(get_mult(140))
    print(get_mult(70))
    print(get_mult(11))
    user_send = int(input("Введите число: "))
    print(
        f"Простые множители числа {user_send} приведены в списке: {get_mult(user_send)}")


if __name__ == '__main__':
    main()
