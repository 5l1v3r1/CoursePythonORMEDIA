import re

print("-------------------------------------------- Методы объекта строка")

text = "I Love You!"
print("Исходная строка:", text)
print("Возвращает номер первого вхождения:", text.rfind("Love"))
print("Возвращает номер первого вхождения:", text.index("Love"))
print("Заменяет символы из строки, на указанные:", text.replace("Love", "LOVE"))
print("Разрезает строку в месте введенного символа:", text.split(" "))

print("-------------------------------------------- Табуляция и Новая строка")

# Табуляция
print("Бла, бла, бла\t123456")
print("Бла, бла, бла\t000000")
# Новая строка
print("Привет\nМир")

print("-------------------------------------------- Сырая строка")

text1 = r'C:\newt.txt'  # Сырая (\n - игнорируется)
text2 = 'C:\newt.txt'  # Обычная (\n - переводит на новую строку)
print(text1, text2)

print("-------------------------------------------- Регулярные выражения")

text = "Hello world. Python Lesson. Python 666."
print("Исходная строка:", text, "\n")

# Методы регулярных выражений
print("[re.match] (ищет в начале строки, возвращает только 1-ое совпадение): ", re.match(r"Hel", text))
print("[re.search] (ищет по всей строке, возвращает только 1-ое совпадение): ", re.search(r"Pyt", text))
print("[re.findall] (ищет по всей строке, возвращает все совпадения):        ", re.findall("Python", text))
print("[re.sub] (заменяет символы из строки, на указанные:):                 ", re.sub(r"Python", "PYTHON", text))
print("[re.split] (разрезает строку в месте введенного символа):             ", re.split(r" ", text, maxsplit=0))
print("[re.compile] (создание отдельного объекта для использования в поиске):", re.compile("Pyt"))
print()

# Применение специальных символов (операторов)
print(r"[.]    (Люьой символ):                ", re.findall(r".orld", text))
print(r"[\w\W] (Любая цифра/буква):           ", re.findall(r"Python\W\w\w\w", text))
print(r"[\d\D] (Любая цифра):                 ", re.findall(r"Python\D\d\d\d", text))
print(r"[\s\S] (Любой пробел):                ", re.findall(r"Python\s", text))
print(r"[ 6]   (Любой из символов в скобке):  ", re.findall(r"Python[ 6][ 6][ 6][ 6]", text))
