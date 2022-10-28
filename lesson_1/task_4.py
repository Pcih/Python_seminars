"""
Task_4
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""


def get_quarter():
    try:
        quarter = float(input('Ведите четверь осей кординат: '))
        return quarter
    except:
        print('Вы вели не число!!!')


def define_quarter(number):
    dict_quarter = {
        1: 'x > 0, y > 0',
        2: 'x > 0, y < 0',
        3: 'x < 0, y < 0',
        4: 'x < 0, y > 0'
    }
    try:
        return dict_quarter[number]
    except:
        return 'Такой четверти не существует'


def main():
    return define_quarter(get_quarter())


print(main())
# И прошу заметить ни каких условий
# решил попробовать так решить задачу
# но мог при помощи услови но так мне показалось интересней
