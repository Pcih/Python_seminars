"""
Task_3
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
 [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
from random import uniform


def random_list():
    return [round(uniform(-99.999, 100), 3) for x in range(11)]


def get_max_idx(my_list: list):
    ACCURACY_CONSTANT = 1
    max_number = my_list[0]
    max_idx = 0

    for i in range(len(my_list) - ACCURACY_CONSTANT):
        if max_number < my_list[i]:
            max_number = my_list[i]
            max_idx = i
    return max_idx


def get_min_idx(my_list: list):
    ACCURACY_CONSTANT = 1
    min_number = my_list[0]
    min_idx = 0

    for i in range(len(my_list) - ACCURACY_CONSTANT):
        if min_number > my_list[i]:
            min_number = my_list[i]
            min_idx = i
    return min_idx


def main():
    new_list = random_list()
    max_idx = get_max_idx(new_list)
    min_idx = get_min_idx(new_list)
    res_number = new_list[max_idx] - new_list[min_idx]
    print(f'Изначальный список\n{new_list}\n\
max={new_list[max_idx]} min={new_list[min_idx]}\n\
разница между максимальным и минимальным значением {res_number}')

    # Можно решить все в одну строчку
    print(max(new_list) - min(new_list))


if __name__ == '__main__':
    main()
