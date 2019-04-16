print("-------------------------------------------- Создание класса. Создание экзепляра. Процедура инициализации.")


# Класс  — тип, описывающий устройство объектов.
# Объект — это экземпляр класса. Объект-представитель определенного класса.
# Атрибусы класса - переменные и данные класса
# Методы класса - функции класса

class Movie:
    valueMax = 100
    valueMin = 5

    # Выполнится при создании экземпляра
    def __init__(self):
        print("Экземпляр класса создан")


# Создание экземпляра класса "Movie()" под именем "x"
x = Movie()

# Вывод данных без создния экзепляра
print(Movie.valueMin, Movie.valueMax)

# Вывод данных экземпляра "x"
print(x.valueMin, x.valueMax)

print("-------------------------------------------- Класс Orange(Апельсин). Создание экхемпляров. Метод очистки.")


class Orange:
    def __init__(self, color, size, view):
        self.color = color
        self.size = size
        self.view = view
        print("Аппельсин создан")
        print("Его параметры:", "ЦВЕТ:", self.color, "РАЗМЕР:", self.size, "ВНЕШНИЙ ВИД:", self.view)

    # Метод "Очистить кожуру"
    def peelOff(self):
        self.view = "Очищен от кожуры"
        print("Параметры:", "ЦВЕТ:", self.color, "РАЗМЕР:", self.size, "ВНЕШНИЙ ВИД:", self.view)


# Создаем наши апельсины
oneOrange = Orange("черный", "большой", "без дефектов")
twoOrange = Orange("оранжевый", "средний", "помятый")
threeOrange = Orange("красный", "маленький", "без дефектов")

# Чистим наши апельсины
oneOrange.peelOff()
twoOrange.peelOff()
threeOrange.peelOff()
