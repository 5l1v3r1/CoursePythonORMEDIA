print("-------------------------------------------- Задание 1 (77)")


def func1():
    print("[Простая функция]")


func1()

print("-------------------------------------------- Задание 2 (77)")


def func2(a):
    print("[Функция с аргументом] a =", a, "умноженное на 2 равно:", a * 2)


func2(5)

print("-------------------------------------------- Задание 3 (77)")


def func3(a):
    if a % 2 == 0:
        res = "yes"
    else:
        res = "no"
    print("[Функция с аргументом]", a, "Четное число?", res)


func3(8)

print("-------------------------------------------- Задание 4 (78)")


def func4(a, b):
    if a > b:
        res = "yes"
    else:
        res = "no"
    print("[Функция с 2-умя аргументами]", a, ">", b, res)


func4(15, 10)

print("--------------------????------------------------ Задание 5 (78)")

func5 = lambda a, b: a % 2 and b % 2
print(func5(5, 3))

print("-------------------------------------------- Задание ?? (78)")
print("[Функция поиска минимума и максимума в списке]")
sps = [1, 5, 4, 3, 7, 8, 4, 6, 5, 9, 0, 0, 3, 1, 2]
print(" Исходный список:", sps)


def func5(a):
    a = sorted(a)
    print(" Минимальное число:", a[0], "\n Максимальное число:", a[-1])


func5(sps)

print("-------------------------------------------- Задание ?? (78)")
print("[Функция вовращает пору года по числу месяца]")


def season(num_month):
    print(" Исходный номер месяца:", num_month)
    if 9 <= num_month <= 11:
        print(" Пора года: Осень")
    elif 12 == num_month <= 2:
        print(" Пора года: Зима")
    elif 3 <= num_month <= 5:
        print(" Пора года: Весна")
    elif 6 <= num_month <= 8:
        print(" Пора года: Лето")
    else:
        print(" Некректное число")


season(9)

print("-------------------------------------------- Задание ?? (78)")
print("[Функция возвращает True - дата существует, False - дата не существует]")


def data(day, month, year):
    flag = "False"
    print(" Исходный дата:", day, ".", month, ".", year)
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12):
        if (1 <= day <= 31):
            flag = "True"
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11):
        if (1 <= day <= 30):
            flag = "True"
    elif (month == 2):
        if (1 <= day <= 28):
            flag = "True"
    else:
        flag = "False"
    print()


data(22, 1, 1996)
