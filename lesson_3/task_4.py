"""
Task_4
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
 45 -> 101101
 3 -> 11
 2 -> 10
"""

# При помощи рекурсии


def decimalToBinary(n):
    if(n > 1):
        decimalToBinary(n//2)
    print(n % 2, end='')

# При помощи встроиной функции


def decimalToBinary_bin(n):
    return bin(n).replace("0b", "")


def main():
    decimalToBinary(45)
    print("\n")
    decimalToBinary(3)
    print("\n")
    decimalToBinary(2)
    print("\n")
    print(decimalToBinary_bin(45))
    print(decimalToBinary_bin(3))
    print(decimalToBinary_bin(2))


if __name__ == '__main__':
    main()
