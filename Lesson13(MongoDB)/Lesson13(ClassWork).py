from ClassLawr_MongoDB import MongoDB

# Используется локальная база данных на MacOS
# Для просмотра используется: MongoDB Compass

print("-------------------------------------------- Тестирование своего класса MongoDB")

# string = "mongodb+srv://Admin:P13hesheshes@botonlnr-h6f2t.mongodb.net/test?retryWrites=true&w=majority"
string = "localhost:27017"

# Подключение
print()
BD = MongoDB(connection_string=string, ssl=False)

# Удаление Коллекции (если не существует ничего не происходит)
print()
BD.delete_collection(dbs='ClassLawr_MongoDB', collection='OneCollection')
BD.delete_collection(dbs='ClassLawr_MongoDB', collection='TwoCollection')

# Создание Базы данных + Коллекция (При добавлении данных создается автоматически)
print()
BD.add_line_to_end('ClassLawr_MongoDB', 'OneCollection', {'name': 'user 1', 'level': 1})
BD.add_line_to_end('ClassLawr_MongoDB', 'OneCollection', {'name': 'user 2', 'level': 2})
BD.add_line_to_end('ClassLawr_MongoDB', 'TwoCollection', {'name': 'user 3', 'level': 3})
BD.add_line_to_end('ClassLawr_MongoDB', 'TwoCollection', {'name': 'user 4', 'level': 4})
BD.add_line_to_end('ClassLawr_MongoDB', 'TwoCollection', {'name': 'user 5', 'level': 5})

# Показать что содержиться внутри "database"
print()
BD.nice_print(BD.show_database(dbs='ClassLawr_MongoDB'))

# Показать что содержиться внутри "collection"
print()
BD.nice_print(BD.show_collection(dbs='ClassLawr_MongoDB', collection='OneCollection'))
BD.nice_print(BD.show_collection(dbs='ClassLawr_MongoDB', collection='TwoCollection'))

# Проверка существует ли Коллекци (True, False)
print()
print("-> Существует?", BD.check_collection(dbs='ClassLawr_MongoDB', name_collection='OneCollection'))

# Удаление всех документов в коллекции
print()
BD.clear_collection(dbs='ClassLawr_MongoDB', collection='TwoCollection')

# Удаление последнего документа в коллекции
print()
BD.del_line_to_end(dbs='ClassLawr_MongoDB', collection='OneCollection')