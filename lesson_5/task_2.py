"""
Task_2
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
"""

from secrets import choice
candy = 2021
player_1_candy = 0
player_2_candy = 0
left_candy = 2021
lottery = [1,2]
lottery_choice = choice(lottery)
i=0
j=0
print('Добро пожаловать в игру!')
name_firht = input('Имя первого игрока: ')
name_second = input('Имя второго игрока: ')
print('Игрок',name_firht, 'начинает', lottery_choice,'- ым')
while i <= candy:
    player_1 = int(input('Первай игрок, ходите!'))
    while player_1 > 28 or player_1 <= 0:
        print('Вы взяли количество конфет не соответствующее условию игры, пробуйте ещё')
        player_1 = int(input('Ход первого игрока! Смелее!: '))
    if i + player_1 == candy:
            player_1_candy = player_1_candy + player_1 + player_2_candy
            player_2_candy = 0
            print('Победил игрок номер один,','у него - ', player_1_candy, 'конфет')
            break
    j= j + player_1

    while j>candy:
        print('Это очень много!!!! Повторите попытку:')
        j = j - player_1
        player_1 = int(input('Ход первого игрока! Помните!! Не более 28 конфет!: '))
        j = j + player_1
        if i + player_1 == candy:
            player_1_candy = player_1_candy + player_1 + player_2_candy
            player_2_candy = 0
            print('Победил первый игрок,','у которого - ', player_1_candy, 'конфет')
            break


    player_1_candy = player_1_candy + player_1
    left_candy = left_candy - player_1
    print('Осталось', left_candy, player_1_candy)


    player_2 = int(input('Ход второго игрока! Какое количество возьмёте?: '))
    while player_2 > 28 or player_1 <= 0:
        print('Это пребор! Попробуйте ещё раз! Помните! Не более 28')
        player_2 = int(input('Ход второго игрока! Сколько желаете?: '))
    j = j + player_2

    while j>candy:
        j = j - player_2
        print('Ого! Это слишком много. Аппетит нужно придержать:')
        player_2 = int(input('Ход второго игрока! Сколько возьмете на этот раз?: '))
        j = j + player_2
        if i + player_2 == candy:
            player_2_candy = player_2_candy + player_2 + player_1_candy
            player_1_candy = 0
            print('Победил  второй игрок,',' с результатом - ', player_2_candy, 'конфет')
            break
    i = player_1_candy + player_2_candy
    if i + player_2 == candy:
            player_2_candy = player_2_candy + player_2 + player_1_candy
            player_1_candy = 0
            print('Победил второй игрок,','с результатом - ', player_2_candy, 'конфет')
            break

    player_2_candy = player_2_candy + player_2

    left_candy = left_candy - player_2
    print('Осталось', left_candy, ':( конфет!',player_2_candy)

print('колличество конфет у первого игрока', player_1_candy)
print('колличество конфет у второго игрока', player_2_candy) 