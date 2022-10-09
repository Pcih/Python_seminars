from random import randint, shuffle

lst = [randint(0, 10) for i in range(randint(5, 20))]
print(f"исходный список:\n{lst}")
shuffle(lst)
print(f"список после перемешивания:\n{lst}")


def mix_list(list_original):
    list = list_original[:]
    list_length = len(list)
    for i in range(list_length):
        index_aleatory = randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    return list


print(f'список после перемешивания с помощью функции:\n{mix_list(lst)} ')
