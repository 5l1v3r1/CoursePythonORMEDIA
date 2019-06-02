from pymongo import MongoClient

# Подключение к БД которая по умолчанию
client = MongoClient('mongodb://localhost:27017/')
print(client)

# Создать БД
db = client['test-database']
print(db)

# Создание коллекции (похожее на таблицу)
collection = db['test-collection']
print(collection)

users = collection['users']
print(users)

users.save({'name': 'user 1', 'level': 1})

for user in users.find():
    print('->', user)
