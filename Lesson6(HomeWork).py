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

