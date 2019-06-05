from ClassLawrPostgreSQL import PostgreSQL

# Используется локальная база данных на MacOS (Postgres)
# Для просмотра используется: Postico

print("-------------------------------------------- Тестирование своего класса PostgreSQL")

# Создание объекта Базы данных
print()
BD = PostgreSQL('localhost', '5432', 'lawr', 'lawr', 'lawr')

# Создаем таблицу (Если уже есть, то перезапись)
table_settings = """id SERIAL PRIMARY KEY,
                        Cur_Abbreviation text,
                        Cur_Name text,
                        Cur_Scale integer,
                        Cur_OfficialRate real
                        """

BD.delete_table(table='ClassLawr_PostgreSQL')
BD.create_table(table='ClassLawr_PostgreSQL', structure=table_settings)

BD.clear_table(table='ClassLawr_PostgreSQL')
print(BD.show_table(table='ClassLawr_PostgreSQL'))

my_data = [(1, 'бла1', 'бла2', 100, 1.456), (2, 'бла3', 'бла4', 150, 2.854)]
BD.insert_data(table='ClassLawr_PostgreSQL', data=my_data)
print(BD.show_table(table='ClassLawr_PostgreSQL'))

BD.add_line_to_end(table='ClassLawr_PostgreSQL', value=('бла1', 'бла2', 100, 1.456))
print(BD.show_table(table='ClassLawr_PostgreSQL'))

BD.add_line_to_end(table='ClassLawr_PostgreSQL', value=('бла7', 'бла8', 100, 1.456))
print(BD.show_table(table='ClassLawr_PostgreSQL'))

BD.del_line_to_end(table='ClassLawr_PostgreSQL')
print(BD.show_table(table='ClassLawr_PostgreSQL'))
