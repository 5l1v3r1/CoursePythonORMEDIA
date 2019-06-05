from psycopg2 import sql
import psycopg2


# Класс для работы с БД "PostgreSQL"
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
        print("-> Подключение к БД ({})".format(self.DB))

    # Открывать и закрывает КУРСОР (дает право на внесение изменений)
    def open_or_close_cursor(self, status):
        if status == "OPEN":
            self.CURSOR = self.DB.cursor()
        if status == "CLOSE":
            self.CURSOR.close()

    # Возвращает True если таблица существует
    def check_table(self, table):
        for tb in self.show_database():
            if tb[2] == table:
                return True
        return False

    # Создание таблицы
    def create_table(self, table, structure):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('CREATE TABLE ' + table + '(' + structure + ')'))
        self.open_or_close_cursor('CLOSE')

    # Удаление таблицы
    def delete_table(self, table):
        if self.check_table(table):
            self.open_or_close_cursor('OPEN')
            self.CURSOR.execute(sql.SQL('DROP TABLE ' + table))
            self.open_or_close_cursor('CLOSE')

    # Очистка всех строк из таблицы
    def clear_table(self, table):
        if not self.check_table(table):
            self.open_or_close_cursor('OPEN')
            self.CURSOR.execute(sql.SQL('DELETE FROM ' + table))
            self.open_or_close_cursor('CLOSE')

    # Выводит СПИСОК, каждый элемент это КОРТЕЖ (таблица), в КОРТЕЖЕ элементы (параметры таблицы)
    def show_database(self):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('SELECT * FROM information_schema.tables WHERE table_schema=\'public\''))
        list_of_table = self.CURSOR.fetchall()  # Возвращает список всех строк
        self.open_or_close_cursor('CLOSE')
        return list_of_table

    # Выводит СПИСОК, каждый элемент это КОРТЕЖ (строка из таблицы), в КОРТЕЖЕ элементы (ячейки строки)
    def show_table(self, table):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('SELECT * FROM ' + table))
        list_of_strings = self.CURSOR.fetchall()  # Возвращает список всех строк
        self.open_or_close_cursor('CLOSE')
        return list_of_strings

    # Заполнение таблицы данными из "data"
    def insert_data(self, table, data):
        self.open_or_close_cursor('OPEN')
        with self.DB.cursor() as self.CURSOR:
            values_sql = sql.SQL(',').join(map(sql.Literal, data))
            two = sql.SQL('INSERT INTO ' + table + ' VALUES {}').format(values_sql)
            self.CURSOR.execute(two)
        self.open_or_close_cursor('CLOSE')

    # Добавление строки "value" в конец таблицы "table"
    def add_line_to_end(self, table, value):
        self.open_or_close_cursor('OPEN')
        last_record_id = len(self.show_table(table))
        my_tuple = ((last_record_id + 1), value[0], value[1], value[2], value[3])
        my_list = [my_tuple]
        with self.DB.cursor() as self.CURSOR:
            values_sql = sql.SQL(',').join(map(sql.Literal, my_list))
            two = sql.SQL('INSERT INTO ' + table + ' VALUES {}').format(values_sql)
            self.CURSOR.execute(two)
        self.open_or_close_cursor('CLOSE')

    # Удаление строки в конеце таблицы
    def del_line_to_end(self, table):
        last_record_id = len(self.show_table(table))
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('DELETE FROM ' + table + ' WHERE id = ' + str(last_record_id)))
        self.open_or_close_cursor('CLOSE')
