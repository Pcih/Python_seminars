"""
Task_2a
Условие (а)
Человек против bot
"""

from random import *
import os


os.system("cls")

greeting = ('Приветствую Вас! \n'
            'Начнём!\n')

messages = ['Ваша очередь',  'Берите конфеты',
            'Смелее']


def candy(n): 
    if n == 1 or (n % 10 == 1 and n > 20):
        return 'а'
    elif 1 < n < 5 or 1 < n % 10 < 5:
        return 'ы'
    else:
        return ''
def introduce_players():
    player1 = input('Как Вас зовут? ')
    player2 = 'Юрий'
    print(f'Меня  {player2}\n')
    return [player1, player2]


def get_rules(players):
    n = int(input('Какое колличество конфет на кону? '))
    m = int(input('Максимально за один ход? '))
    first = input(
        f'{players[0]}, есть желание ходить первым, тогда жми 1. Нет? Любую другую клавишу ')
    if first != '1':
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2] 
    while rules[0] > 0:
        max = rules[1]
        if max > rules[0]: 
            max = rules[0]
        if not count % 2:   
            move = randint(1, max)
            print(f'беру {move} ')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Ого! это очень много, можно не более {rules[1]} конфет{candy(rules[1])}, у нас всего {rules[0]} конфет{candy(rules[0])}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Пробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'У Вас не осталось попыток. Конец игры!')
        rules[0] -= move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{candy(rules[0])}')
        else:
            print('Конфеты закончились.')
        count += 1
    return players[count % 2]

    
print(greeting)
players = introduce_players()
rules = get_rules(players)
winer = play_game(rules, players, messages)
print(f'В этот раз победил {winer}! Молодец! \n')