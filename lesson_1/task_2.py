"""
Task_2
Напишите программу для. проверки истинности утверждения
 ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
"""


print("x y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z)) == (not x or not y or not z):
                print("Утверждение истинно")


# Второй вариант для интересса
# def inputNumbers(x=3):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     return (not (x[0] or x[1] or x[2])) == (not x[0] and not x[1] and not x[2])


# statement = inputNumbers()

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")
