print("-------------------------------------------- Переменные")

# Присвайвание
number = 1
text = " ThisIsText"

# Пустая переменная None
x = None
print(x)
x = 5
print(x)

# Соединяем число и текст (нужно привести к одному строковому типу)
result = str(number) + text
print(result)

# Инкремент и Декремент
a = 5
a += 5
b = a
b -= 4
print(a, b, end=" (или так) ")
print(str(a) + " " + str(b))

# Калькулятор (простой, только сложение)
print("Введите два числа которые нужно сложить:")
x = input()
y = input()
result = int(x) + int(y)
print("Результат сложения: ", result)

# Множественное присвайвание
a = 10
b = 20
a, b = b, a
print(a, b)