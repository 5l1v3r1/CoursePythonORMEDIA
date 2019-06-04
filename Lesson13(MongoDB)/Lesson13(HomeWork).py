from ClassLawrMongoDB import MongoDB
import Lesson07LawrParserNBRB

print("-------------------------------------------- Задание 1 (67)")

'''
Создать бд с данными о курсах валют за последние 20 лет (Немного поменял условие, уж очень было интересно).
'''

# Создание объекта Базы данных
lawr = MongoDB("mongodb+srv://Admin:P13hesheshes@botonlnr-h6f2t.mongodb.net/test?retryWrites=true&w=majority")

# Получаем такущую дату (можно было проще, но сделал через свой класс, что был под рукой)
rates = Lesson07LawrParserNBRB.LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
data = rates.update_json()[0]['Date'][0:10].replace("-", "")  # Имеет вид: 20190507
del rates

# Разбиваем дату на переменные для удобства
year = int(data[0:4])
month = data[4:6]
day = data[6:9]

for i in range(20 + 1):  # Цикл от 0 до 20
    # Формируем название таблицы на основе даты
    name_collection = 'rates' + str(year - i) + str(month) + str(day)
    # Создаем таблицу (Если уже есть, то перезапись)
    lawr.delete_collection('Test', name_collection)
    # Создаем объект с курсами валют на определенную дату
    rates = Lesson07LawrParserNBRB.LawrParserNBRB(
        "http://www.nbrb.by/API/ExRates/Rates?onDate={}-{}-{}&Periodicity=0".format(year - i, month, day))

    # Заполненяем таблицу объектом (с курсами валют)
    for line in rates.update_json():  # Цикл по линиям (словарям) c 1-ой валюты по последнюю
        lawr.add_line_to_end('Test', name_collection, {'Cur_Abbreviation': line['Cur_Abbreviation'],
                                                       'Cur_Name': line['Cur_Name'],
                                                       'Cur_Scale': line['Cur_Scale'],
                                                       'Cur_OfficialRate': line['Cur_OfficialRate']})
    lawr.nice_print(lawr.show_collection('Test', name_collection))

    del rates  # Удаляем объект (так как в цикле он будет создаваться заново)
