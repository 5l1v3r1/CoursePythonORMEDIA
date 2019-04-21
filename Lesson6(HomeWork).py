print("-------------------------------------------- Задание 1 (88)")

'''
Определите класс Apple с четырьмя переменными экземпляра, представляющими четыре свойства яблока.
'''


class Apple:
    def __init__(self, color, size, view, sort):
        self.color = color
        self.size = size
        self.view = view
        self.sort = sort
        print("Яблоко создано")
        print("Его параметры:", "ЦВЕТ:", self.color, "РАЗМЕР:", self.size, "ВНЕШНИЙ ВИД:", self.view, "СОРТ:",
              self.sort)


Apple1 = Apple("черный", "большой", "без дефектов", "летний")
Apple2 = Apple("черный", "большой", "помятое", "осенний")
Apple3 = Apple("черный", "большой", "гнилое", "зимний")

print("-------------------------------------------- Задание 2 (88)")

'''
Создайте класс Circle с методом area, подсчитывающим и возвращающим площадь круга. Затем создайте объект Circle,
вызовите в нем метод area и выведите результат. Воспользуйтесь функцией pi из встроенного в Python модуля math.
'''


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius * self.radius


littleCircle = Circle(5)
print(littleCircle.area(), "см * см")
bigCircle = Circle(10)
print(bigCircle.area(), "см * см")

print("-------------------------------------------- Задание 3 (89)")

'''
Есть класс Person, конструктор которого принимает три параметра (не учитывая self) – имя, 
фамилию и квалификацию специалиста. Квалификация имеет значение заданное по умолчанию, равное единице.
У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.
'''


class Person:
    def __init__(self, name, surname, specialistQualification=1):
        self.name = name
        self.surname = surname
        self.specialistQualification = specialistQualification

    def printInfo(self):
        print("Имя:", self.name, "; Фамилия:", self.surname, "; Квалификация:", self.specialistQualification)


Person1 = Person("Игорь", "Юдин")
Person1.printInfo()
Person2 = Person("Игорь", "Юдин", 3)
Person2.printInfo()

print("-------------------------------------------- Задание 4 (91)")

'''
Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника. 
Затем создайте объект Triangle, вызовите в нем area и выведите результат
'''


class Triangle:
    def semi_perimeter(self):  # Полупериметр
        self.p = 0.5 * (self.a + self.b + self.c)
        return self.p

    def area(self):  # Площадь
        import math
        return math.sqrt(self.p * (self.p - self.a) * (self.p - self.b) * (self.p - self.c))

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.semi_perimeter()


littleTriangle = Triangle(5, 6, 7)
print(round(littleTriangle.area(), 3), "см * см")
bigTriangle = Triangle(10, 14, 15)
print(round(bigTriangle.area(), 3), "см * см")

print("-------------------------------------------- Задание 5-6 (92)")

'''
Создайте классы Rectangle(Прямоугольник) и Square(Квадрат) с методом calculate_perimeter, вычисляющим периметр фигур,
которые эти классы представляют. Создайте объекты Rectangle и Square вызовите в них этот метод.
'''

'''
В классе Square определите метод change_size, позволяющий передавать ему число, 
которое увеличивает или уменьшает (если оно отрицательное) каждую сторону объекта Square на соответствующее значение
'''


class Rectangle:
    def calculate_perimeter(self):  # Площадь
        return (self.a * self.a) + (self.b * self.b)

    def __init__(self, a, b):
        self.a = a
        self.b = b


class Square:
    def calculate_perimeter(self):  # Площадь
        return self.a * 4

    def change_size(self, x):
        self.a = self.a + x

    def __init__(self, a):
        self.a = a


One = Rectangle(5, 6)
print(round(One.calculate_perimeter(), 3), "см")
Two = Square(4)
print(round(Two.calculate_perimeter(), 3), "см")
Two.change_size(2)
print(round(Two.calculate_perimeter(), 3), "см")


