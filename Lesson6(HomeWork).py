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
print(littleCircle.area(), "см")
bigCircle = Circle(10)
print(bigCircle.area(), "см")

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
Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника. Затем создайте объект Triangle, вызовите в нем area и выведите результат
'''

