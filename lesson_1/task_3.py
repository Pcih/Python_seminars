"""
Task_3
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
Пример:
  ◦ x=34; y=-30 -> 4
  ◦ x=2; y=4-> 1
  ◦ x=-34; y=-30 -> 3

"""


def get_coordinates():
    try:
        x = int(input('Ведите точку Х: '))
        y = int(input('Ведите точку Y: '))
        if x != 0 and y != 0:
            return x, y
    except:
        print('Вы вели не то число или вобще не число')


def get_result(number):
    try:
        if number[0] > 0 and number[1] > 0:
            print('I четверть.')
        elif number[0] > 0 and number[1] < 0:
            print('II четверть.')
        elif number[0] < 0 and number[1] < 0:
            print('III четверть.')
        elif number[0] < 0 and number[1] < 0:
            print('VI четверть.')
    except:
        print('Error data:')


get_result(get_coordinates())
