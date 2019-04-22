import re

print("-------------------------------------------- Задание 1 (62)")

'''
1) Вернуть первое слово из строки
'''

string = "Hello world!!!"
result = re.split(r' ', string)
print(result)  # Список
print(result[0])  # Первый элемент списка

print("-------------------------------------------- Задание 2 (62)")

'''
2) Вернуть первые два символа каждого слова
'''

string = "Hello world!!!"
result = re.split(r' ', string)
print(result)  # Список
for i in result:
    print(i[0], "" + i[1])  # Первый элемент списка

print("-------------------------------------------- Задание 3 (62)")

'''
4) Извлечь дату из строки
'''

domens = ["dwef543r@mail.ru", "wef4@gmail.com", "wewewe@mail.ru"]
for i in domens:
    result = re.search(r'@', i)
    print(result, " - ", result.span(), " - ", i[result.span()[1]:])

print("-------------------------------------------- Задание 5 (62)")

'''
4) Извлечь дату из строки
'''

string = "После обращения Юрия Левитана 22.06.1941 Название «Великая Отечественная война» стало использоваться в СССР"
# Отдельные слова
result = re.split(r' ', string)  # Отдельные слова
print(result)
# Поиск точки
for i in result:
    result = re.search(r'\.', i)
    #if result.group()
    print(result.group(0), " - ")
