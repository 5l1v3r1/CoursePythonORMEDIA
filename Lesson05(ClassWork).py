print("-------------------------------------------- Функция с необязательным параметром")


def prim1(a, b, c=6):  # Если не задан то =6, если задан явно то будет иметь значение аргумента.
    pass  # Пустая операция (ничего не происходит)
    return print(a * b + c)


print("ИСХ: prim1(2, 4) и prim1(2, 4, 8)")
prim1(2, 4)  # Задан
prim1(2, 4, 8)  # Не Задан

print("-------------------------------------------- Вызов функции с именнованными аргументами")

print("ИСХ: prim1(b=2, a=6, c=5)")
prim1(b=2, a=6, c=5)

print("-------------------------------------------- Пример Map (Операции над элементами)")

numbers = [1, 2, 3, 4, 5]
MultiplyBy2 = lambda x: x * 2
numbers_result = list(map(MultiplyBy2, numbers))
print("ИСХ: numbers =", numbers, "и Функция: MultiplyBy2 (x * 2)")
print("РЕЗ: list(map(MultiplyBy2, numbers)) =", numbers_result)

print("-------------------------------------------- Пример Filter (Фильтр/Отбор элементов)")

numbers = [1, 2, 3, 4, 5]
MoreThan3 = lambda x: (x > 3)
numbers_result = list(filter(MoreThan3, numbers))
print("ИСХ: numbers =", numbers, "и Функция: MoreThan3 (x > 3)")
print("РЕЗ: list(filter(MoreThan3, numbers)) =", numbers_result)

print("-------------------------------------------- Декоратор (Модификация имеющейся функции)")


def decorator(func):
    def wrapper():
        print("Один")
        func()
        print("Три")

    return wrapper


@decorator
def show():
    print("Два")


show()

print("-------------------------------------------- Пример использования *args / **kwargs ")


# 1 Ситуация
def many(*args, **kwargs):
    print("Кортеж - ", args)
    print("Словарь -", kwargs)


many(1, 2, 3, 4, 5, name="Igor", job="Programmer", sex="Male")


# 2 Ситуация
def name(name1, name2, name3):
    print("1-ый аргумент:", name1)
    print("2-ой аргумент:", name2)
    print("3-ий аргумент:", name3)


name(*["Коля", "Маша", "Игорь"])

print("-------------------------------------------- Lambda (Мини функция)")

lam1 = lambda x, y, z: x * y + z
print("Пример Lambda (x * y + z):", lam1(2, 3, 4))
