"""
Task_2
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
 [2, 3, 4, 5, 6] => [12, 15, 16];
 [2, 3, 5, 6] => [12, 15]
"""
from random import randint


def random_list(send_user):
    return [randint(0, 10) for _ in range(send_user)]


def get_multi(my_list: list):
    res_list = []
    for i in range(len(my_list) // 2):
        first_idx = i
        last_idx = (i + 1) * -1
        multi_num = my_list[first_idx] * my_list[last_idx]
        res_list.append(multi_num)
    return res_list


def get_multi_result(my_list: list):
    mid_idx_cor = len(my_list) % 2
    mid_idx = len(my_list) // 2
    if mid_idx_cor == 0:
        res_list = get_multi(my_list)
    else:
        res_list = get_multi(my_list)
        multi_num = my_list[mid_idx] * my_list[mid_idx]
        res_list.append(multi_num)
    return res_list


def main():
    user_number = int(input('Ведите натуральное число: '))
    new_list = random_list(user_number)
    result_list = get_multi_result(new_list)
    print(f'Изначальный список\n{new_list}\n\
 Список произведений\n{result_list}')


if __name__ == '__main__':
    main()
