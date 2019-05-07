import psycopg2
from psycopg2 import sql
import requests


# Класс для работы с БД
class PostgreSQL:
    # Инициализаци/открытие БД
    def __init__(self, host, port, user, password, dbname):
        self.DB_HOST = host
        self.DB_PORT = port
        self.DB_USER = user
        self.DB_PASS = password
        self.DB_NAME = dbname
        self.DB = psycopg2.connect(dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASS, host=self.DB_HOST,
                                   port=self.DB_PORT)
        # Когда значение равно True, каждый вызов execute будет моментально отражен на стороне БД
        self.DB.autocommit = True
        self.CURSOR = self.DB.cursor()

    # Открывать и закрывает КУРСОР (дает право на внесение изменений)
    def open_or_close_cursor(self, status):
        if status == "OPEN":
            self.CURSOR = self.DB.cursor()
        if status == "CLOSE":
            self.CURSOR.close()

    # Возвращает True если таблица существует
    def check_table(self, name_table):
        for table in self.show_database():
            if table[2] == name_table:
                return True
        return False

    # Создание таблицы
    def create_table(self, name_table, my_data):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('CREATE TABLE ' + name_table + '(' + my_data + ')'))
        self.open_or_close_cursor('CLOSE')

    # Удаление таблицы
    def delete_table(self, name_table):
        if self.check_table(name_table):
            self.open_or_close_cursor('OPEN')
            self.CURSOR.execute(sql.SQL('DROP TABLE ' + name_table))
            self.open_or_close_cursor('CLOSE')

    # Очистка всех строк из таблицы
    def clear_table(self, name_table):
        if not self.check_table(name_table):
            self.open_or_close_cursor('OPEN')
            self.CURSOR.execute(sql.SQL('DELETE FROM ' + name_table))
            self.open_or_close_cursor('CLOSE')

    # Выводит СПИСОК, каждый элемент это КОРТЕЖ (таблица), в КОРТЕЖЕ элементы (параметры таблицы)
    def show_database(self):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('SELECT * FROM information_schema.tables WHERE table_schema=\'public\''))
        list_of_table = self.CURSOR.fetchall()  # Возвращает список всех строк
        self.open_or_close_cursor('CLOSE')
        return list_of_table

    # Выводит СПИСОК, каждый элемент это КОРТЕЖ (строка из таблицы), в КОРТЕЖЕ элементы (ячейки строки)
    def show_table(self, name_table):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('SELECT * FROM ' + name_table))
        list_of_strings = self.CURSOR.fetchall()  # Возвращает список всех строк
        self.open_or_close_cursor('CLOSE')
        return list_of_strings

    # Заполнение таблицы данными из "my_data"
    def insert_data(self, name_table, my_data):
        self.open_or_close_cursor('OPEN')
        with self.DB.cursor() as self.CURSOR:
            values_sql = sql.SQL(',').join(map(sql.Literal, my_data))
            two = sql.SQL('INSERT INTO ' + name_table + ' VALUES {}').format(values_sql)
            lawr.CURSOR.execute(two)
        self.open_or_close_cursor('CLOSE')

    # Добавление строки "my_value" в конец таблицы
    def add_line_to_end(self, name_table, my_value):
        self.open_or_close_cursor('OPEN')
        last_record_id = len(self.show_table(name_table))
        my_tuple = ((last_record_id + 1), my_value[0], my_value[1], my_value[2], my_value[3])
        my_list = [my_tuple]
        with self.DB.cursor() as self.CURSOR:
            values_sql = sql.SQL(',').join(map(sql.Literal, my_list))
            two = sql.SQL('INSERT INTO ' + name_table + ' VALUES {}').format(values_sql)
            lawr.CURSOR.execute(two)
        self.open_or_close_cursor('CLOSE')

    # Удаление строки в конеце таблицы
    def del_line_to_end(self, name_table):
        last_record_id = len(self.show_table(name_table))
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('DELETE FROM ' + name_table + ' WHERE id = ' + str(last_record_id)))
        self.open_or_close_cursor('CLOSE')


# Класс отвечающий за парсинг/отображение/вывод валют
class ParserNBRB:
    JSON = None  # Ответ от сайта в JSON формате (все курсы валют)
    FILE_JSON = None  # Объект открытого файла Lesson7(ClassWork).json

    # Инициализаци/создание парсера
    def __init__(self, URL):
        self.URL = URL

    # Получить JSON
    def update_json(self):
        self.JSON = requests.get(self.URL).json()
        return self.JSON

    # ЗАПИСАТЬ JSON В ФАЙЛ (с форматирование)
    def write_json(self, filename='Lesson7(HomeWork).json'):
        import json
        # Создаем object_filename(открытый для записи файловый объект) привязанный к файлу "filename"
        with open(filename, 'w') as self.FILE_JSON:
            # Метод который записывает в object_filename(файловый объект) данные JSON
            json.dump(self.JSON, self.FILE_JSON, indent=2, ensure_ascii=False)
        return self.FILE_JSON

    # Ищет и возвращает словарь с валютой найденной по "Abbreviation"
    def get_money(self, abbreviation):
        for cur in self.JSON:
            if cur['Cur_Abbreviation'] == abbreviation:
                return cur

    # Преобразоввывает "cur"(словарь с нужной валютой) в удбно читаемый текст
    @staticmethod
    def print_money(cur):
        cur_scale = str(cur['Cur_Scale'])
        cur_abbreviation = str(cur['Cur_Abbreviation'])
        cur_official_rate = str(cur['Cur_OfficialRate'])
        the_details = '\n(' + str(cur['Cur_Name']) + ')'
        text = cur_scale + ' ' + cur_abbreviation + ' = ' + cur_official_rate + ' BYR' + the_details
        return text

    # Возвращает текс /help и /start
    def print_help(self):
        text = 'ОТОБРАЖЕНИЕ КУРСА ВАЛЮТ\n(Национальный Банк РБ)\n\n   Список команд:\n'
        for cur in self.JSON:
            text = text + '/' + str(cur['Cur_Abbreviation']).swapcase() + ' '
        text = text + "\n\n/help - Помощь"
        return text

    # Возвращает список со всеми абревиатурами валют
    def list_cur_abbreviation(self):
        list_cur_abbreviation = []
        for cur in self.JSON:
            list_cur_abbreviation.append(str(cur['Cur_Abbreviation']))
        return list_cur_abbreviation


print("-------------------------------------------- Задание 1 (87)")

'''
Создать бд с данными о курсах валют за последние 20 лет (Немного поменял условие, уж очень было интересно).
'''

# Создание объекта Базы данных
lawr = PostgreSQL('localhost', '5432', 'lawr', 'lawr', 'lawr')

# Получаем такущую дату (можно было проще, но сделал через свой класс, что был под рукой)
rates = ParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
data = rates.update_json()[0]['Date'][0:10].replace("-", "")  # Имеет вид: 20190507
del rates

# Разбиваем дату на переменные для удобства
year = int(data[0:4])
month = data[4:6]
day = data[6:9]

for i in range(21):  # Цикл от 0 до 4
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
    rates = ParserNBRB(
        "http://www.nbrb.by/API/ExRates/Rates?onDate={}-{}-{}&Periodicity=0".format(year - i, month, day))

    # Заполненяем таблицу объектом (с курсами валют)
    for line in rates.update_json():  # Цикл по линиям (словарям) c 1-ой валюты по последнюю
        lawr.add_line_to_end(name_tb, (line['Cur_Abbreviation'],
                                       line['Cur_Name'],
                                       line['Cur_Scale'],
                                       line['Cur_OfficialRate']))
    print(lawr.show_table(name_table=name_tb))

    del rates  # Удаляем объект (так как в цикле он будет создаваться заново)
