print("-------------------------------------------- Задание 1 (79)")

'''
Даны три числа. Вывести на экран “yes”, если среди них есть одинаковые, иначе вывести “ERROR”;
'''

import random

number = [random.randint(1, 3), random.randint(1, 3), random.randint(1, 3)]
print("Исходные числа: ", number)

flag = "false"  # Флаг. Есть одинаковые?
for i in [0, 1]:
    for j in [1 + i, 2]:
        if number[i] == number[j]:  # [1 vs 2,3] # [2 vs 3]
            flag = "true"
            break
if flag == "true":
    print("yes")
else:
    print("ERROR")

print("-------------------------------------------- Задание 2 (79)")

'''
Даны три числа. Вывести на экран “yes”, если можно взять какие-то два из них и в сумме получить третье;
'''

import random

number = [random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)]
print("Исходные числа: ", number)
if number[0] == number[1] + number[2]:
    print("yes")
elif number[1] == number[0] + number[2]:
    print("yes")
elif number[2] == number[0] + number[1]:
    print("yes")
else:
    print("ERROR")

print("-------------------------------------------- Задание 3 (80)")

'''
Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14;
'''

number = [i for i in range(15)]
sum = number[0]
print("Исходные числа: ", number)
for i in range(1, 15):
    sum = sum + number[i]
print("Сумма чисел: ", sum)

print("-------------------------------------------- Задание 4 (80)")

'''
Распечатывать дни недели с их порядковыми номерами. Кроме того, рядом выводить выходной ли это день или рабочий.
'''

mondayNumber = 1
day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
for i in range(7):
    if (i == 5) or (i == 6) :
        print(day[mondayNumber-1], mondayNumber, "число.", "(Выходной)")
    else:
        print(day[mondayNumber-1], mondayNumber, "число.")
    mondayNumber += 1
