"""
Task_4
Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
2*x*2 + 4*x + 5 = 0
или
2*x^2 + 4*x + 5 = 0
"""

from random import randint

def write_func(k: int):
    
    file = open("res_func.txt", 'w+')
    while k > 1:
        file.write(str(randint(1, 100))+' * x ^'+str(k)+'+')
        k -= 1
    file.write(str(randint(1, 100)) + '*x+' + str(randint(1, 100)) + '=0')
    file.close()



def main():
   user_send = int(input("Введите натуральную степень k = "))
   write_func(user_send)

if __name__ == '__main__':
    main()
