"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""
"""
43 06
"""

var = ['разработка',
       'администрирование',
       'protocol',
       'standard']

for i in var:
    byt_i = i.encode('utf-8')
    print(f'Кодированая строка {byt_i}\n'
          f'Декодированая строка {byt_i.decode("utf-8")}')
    print('*' * 20)
