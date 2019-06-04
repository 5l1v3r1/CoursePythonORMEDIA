from ClassLawrPostgreSQL import PostgreSQL

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
