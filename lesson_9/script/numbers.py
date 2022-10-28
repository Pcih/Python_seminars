"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
Пример:
 пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""


def products_of_numbers(numbers: int):
    ACCURACY_CONSTANT = 1
    count = 1
    res_list = []
    for i in range(1, numbers + ACCURACY_CONSTANT):
        count *= i
        res_list.append(count)
    return res_list


def main():
    try:
        user_send = abs(int(input('Ведите длину списка: ')))
        print(products_of_numbers(user_send))
    except:
        print('Вы вели не число!')


if __name__ == '__main__':
    main()
