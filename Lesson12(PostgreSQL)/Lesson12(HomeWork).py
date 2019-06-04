from ClassLawrPostgreSQL import PostgreSQL
import Lesson07LawrParserNBRB

print("-------------------------------------------- Задание 1 (87)")

'''
Создать бд с данными о курсах валют за последние 20 лет (Немного поменял условие, уж очень было интересно).
'''

# Создание объекта Базы данных
lawr = PostgreSQL('localhost', '5432', 'lawr', 'lawr', 'lawr')

# Получаем такущую дату (можно было проще, но сделал через свой класс, что был под рукой)
rates = Lesson07LawrParserNBRB.LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
data = rates.update_json()[0]['Date'][0:10].replace("-", "")  # Имеет вид: 20190507
del rates

# Разбиваем дату на переменные для удобства
year = int(data[0:4])
month = data[4:6]
day = data[6:9]

for i in range(20+1):  # Цикл от 0 до 20
    # Формируем название таблицы на основе даты
    name_tb = 'rates' + str(year - i) + str(month) + str(day)
    table_settings = """id SERIAL PRIMARY KEY,
                        Cur_Abbreviation text,
                        Cur_Name text,
                        Cur_Scale integer,
                        Cur_OfficialRate real
                        """
    # Создаем таблицу (Если уже есть, то перезапись)
    lawr.delete_table(name_tb)
    lawr.create_table(name_tb, table_settings)

    # Очищаем таблицу
    lawr.clear_table(name_table=name_tb)
    print(lawr.show_table(name_table=name_tb))

    # Создаем объект с курсами валют на определенную дату
    rates = Lesson07LawrParserNBRB.LawrParserNBRB(
        "http://www.nbrb.by/API/ExRates/Rates?onDate={}-{}-{}&Periodicity=0".format(year - i, month, day))

    # Заполненяем таблицу объектом (с курсами валют)
    for line in rates.update_json():  # Цикл по линиям (словарям) c 1-ой валюты по последнюю
        lawr.add_line_to_end(name_tb, (line['Cur_Abbreviation'],
                                       line['Cur_Name'],
                                       line['Cur_Scale'],
                                       line['Cur_OfficialRate']))
    print(lawr.show_table(name_table=name_tb))

    del rates  # Удаляем объект (так как в цикле он будет создаваться заново)
