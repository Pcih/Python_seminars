"""
Task_1
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
 [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
"""

# Старый вариант

from random import randint


def random_lest(send_user):
    return [randint(0, 10) for i in range(randint(5, send_user))]


def sum_list_number(res_list: list):
    sum_numbers = 0
    for i in range(1, len(res_list), 2):
        sum_numbers += res_list[i]
    return sum_numbers


def main():
    user_send = int(input('Ведите длину списка: '))
    random_list = random_lest(user_send)
    sum_result = sum_list_number(random_list)
    print(f'Изначальный список\n\
{random_list}\n Сумма чисел {sum_result}')


if __name__ == '__main__':
    main()

# Новый вариант 
res_list = [randint(0, 10) for i in range(randint(5, 10))]
print(sum(list(filter(lambda x: res_list.index(x)%2, res_list))))