"""
Task_1
Вычислить число Pi c заданной точностью d
*Пример:*
при $d = 0.001, π = 3.141.$
"""
from math import pi

def find_the_coefficient(user_send: str):
    if user_send.find('.') != -1:
        return len(user_send) - 2
    return int(user_send)

def get_decimal(coefficient: int):
    return round(pi, coefficient)


def main():
    user_send = input('Ведит число разряда порядка: ')
    coefficient = find_the_coefficient(user_send)
    print(
        f'Число π округлено до {user_send} порядка и равно {get_decimal(coefficient)}')


if __name__ == '__main__':
    main()
