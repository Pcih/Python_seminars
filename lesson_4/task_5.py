"""
Task_5
Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
Пример:
1 Файл : 2*x2 + 4*x + 5 = 0
2 Файл : 4*x2 + 7*x + 9 = 0
3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
Пример:
1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
2 Файл : 4*x2 + 7*x + 9 = 0
3 Файл: (содержит результат) 2*x3 + 8*x2 + 12
"""


def write_file():
    text1 = open('file1.txt', 'w')  
    text1.write('2x² + 4x + 5 = 0')
    text1.close()

    text2 = open('file2.txt', 'w')  
    text2.write('3x² + 6x + 1 = 0')
    text2.close()


def read_file():
    text_1 = open('file1.txt', 'r') 
    line1 = text_1.read().split('+')    
    line1 = [i.lstrip() for i in line1]
    text_1.close()

    text_2 = open('file2.txt', 'r')
    line2 = text_2.read().split('+')    
    line2 = [i.lstrip() for i in line2]
    text_2.close()
    return line1,  line2 



def write_result(res_list: list):
    line1 = [int(i[0]) for i in res_list[0]]
    line2 = [int(i[0]) for i in res_list[1]]

    line3 = []
    for i in range(3):                       
        line3.append(line1[i] + line2[i]) 

    list = str(line3[0]) + 'x²' + '+' + str(line3[1]) + '+' + str(line3[2])  + '=0' 


    text3 = open('file3.txt', 'w') 
    text3.write(list)
    text3.close()

def main():
   write_file()
   write_result(read_file())

if __name__ == '__main__':
    main()