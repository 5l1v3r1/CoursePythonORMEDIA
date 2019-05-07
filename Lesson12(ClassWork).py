import psycopg2
from psycopg2 import sql


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
            self.CURSOR.execute(two)
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
            self.CURSOR.execute(two)
        self.open_or_close_cursor('CLOSE')

    # Удаление строки в конеце таблицы
    def del_line_to_end(self, name_table):
        last_record_id = len(self.show_table(name_table))
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('DELETE FROM ' + name_table + ' WHERE id = ' + str(last_record_id)))
        self.open_or_close_cursor('CLOSE')


print("-------------------------------------------- Тестирование своего класса PostgreSQL")

# Создание объекта Базы данных
lawr = PostgreSQL('localhost', '5432', 'lawr', 'lawr', 'lawr')

# Создаем таблицу (Если уже есть, то перезапись)
table_settings = """id SERIAL PRIMARY KEY,
                        Cur_Abbreviation text,
                        Cur_Name text,
                        Cur_Scale integer,
                        Cur_OfficialRate real
                        """
lawr.delete_table('test')
lawr.create_table('test', table_settings)

lawr.clear_table('test')
print(lawr.show_table('test'))

data = [(1, 'бла1', 'бла2', 100, 1.456), (2, 'бла3', 'бла4', 150, 2.854)]
lawr.insert_data('test', data)
print(lawr.show_table('test'))

lawr.add_line_to_end('test', ('бла1', 'бла2', 100, 1.456))
print(lawr.show_table('test'))

lawr.add_line_to_end('test', ('бла7', 'бла8', 100, 1.456))
print(lawr.show_table('test'))

lawr.del_line_to_end('test')
print(lawr.show_table('test'))
