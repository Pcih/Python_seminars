"""
Задайте число N, создайте список: [-N, N]. Найдите произведение элементов на указанных позициях. Позиции (случайные)  хранятся в файле file.txt (создаётся во время выполнения кода и зависит от количества элементов в списке) в одной строке одно число.
Пример:
Файл:
4
5
2
N = 3 => [-3, -2, -1, 0, 1, 2, 3]
"""
from random import randint


def get_list(user_send):
    ACCURACY_CONSTANT = 1
    return [i for i in range(-user_send, user_send + ACCURACY_CONSTANT)]


def random_naumber(num):
    new_list = []
    for _ in range(num):
        new_list.append(randint(1, num*2))
    return new_list


def write_file(my_list: list, path):
    with open(path, 'w') as f:
        for i in my_list:
            f.write(f'{str(i)}\n')


def reads_file(path: str):
    with open(path, 'r') as f:
        return [int(line.strip()) for line in f]


def get_mult(first_list: list, second_list: list):
    mult = 1
    for i in second_list:
        mult *= first_list[i]
    return mult


def main():
    path = 'my_text.txt'
    user_send = int(input('Диапозон чисел от -n до n: '))
    user_list = get_list(user_send)
    random_list = random_naumber(user_send)
    write_file(random_list, path)
    read_list = reads_file(path)
    print(get_mult(user_list, read_list))


if __name__ == '__main__':
    main()
