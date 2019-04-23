class Bot:
    FLAG_Debug = 1  # =0..3 (Режимы)
    COUNT_Debug = 1  # Счетчик сообщений от debugging
    JSON = None  # Ответ от бота в JSON формате (все сообщения пользователя)
    FILE_JSON = None  # Объект открытого файла Lesson7(ClassWork).json
    MESSAGE_INCOMING = None  # Сообщение Входящее
    MESSAGE_SENT = None  # Сообщение Отправленное

    # Инициализаци/создание бота
    def __init__(self, token):
        self.TOKEN = token
        self.URL = "https://api.telegram.org/bot" + token + "/"
        self.debugging('__init__')

    # ОБНОВИТЬ JSON
    def update_json(self):
        import requests
        global response_update
        response_update = requests.get(self.URL + "getupdates")
        self.JSON = response_update.json()
        self.debugging('update_json')
        return self.JSON

    # ЗАПИСАТЬ JSON В ФАЙЛ (с форматирование)
    def write_json(self, filename='Lesson7(HomeWork).json'):
        import json
        # Создаем object_filename(открытый для записи файловый объект) привязанный к файлу "filename"
        with open(filename, 'w') as self.FILE_JSON:
            # Метод который записывает в object_filename(файловый объект) данные JSON
            json.dump(self.JSON, self.FILE_JSON, indent=2, ensure_ascii=False)
        self.debugging('write_json')
        return self.FILE_JSON

    # ПОЛУЧАТЬ Сообщения
    def get_message(self, number):
        global n
        n = number
        update_id = self.JSON['result'][n]['update_id']
        chat_id = self.JSON['result'][n]['message']['chat']['id']
        date = self.JSON['result'][n]['message']['date']
        text = self.JSON['result'][n]['message']['text']
        self.MESSAGE_INCOMING = {'chat_id': chat_id, 'update_id': update_id, 'date': date, 'text': text}
        self.debugging('get_message')
        return self.MESSAGE_INCOMING

    # ОТПРАВЛЯТЬ Сообщения
    def send_message(self, chat_id, text):
        import requests
        # 1 ВАРИАНТ
        self.MESSAGE_SENT = {'chat_id': chat_id, 'text': text}
        global response_send
        response_send = requests.post(self.URL + 'sendmessage', json=self.MESSAGE_SENT)
        # 2 ВАРИАНТ
        # requests.get(URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text))
        self.debugging('send_message')
        return self.MESSAGE_SENT

    # Отладка (отображает сообщения и возвраты функций)
    def debugging(self, method_name):
        if (method_name == '__init__') and (self.FLAG_Debug != 0):
            if (self.FLAG_Debug == 1) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "Объект создан!")
                self.COUNT_Debug += 1
        if (method_name == 'update_json') and (self.FLAG_Debug != 0):
            if (self.FLAG_Debug == 1) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "[Запрос] Обновление JSON. [Ответ] :",
                      response_update)
                self.COUNT_Debug += 1
            if (self.FLAG_Debug == 2) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), " RETURN <-", self.JSON)
                self.COUNT_Debug += 1
        if (method_name == 'write_json') and (self.FLAG_Debug != 0):
            if (self.FLAG_Debug == 1) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "JSON записан в файл!")
                self.COUNT_Debug += 1
            if (self.FLAG_Debug == 2) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), " RETURN <-", self.FILE_JSON)
                self.COUNT_Debug += 1
        if (method_name == 'get_message') and (self.FLAG_Debug != 0):
            if (self.FLAG_Debug == 1) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "Сообщение №", n, "вытянуто из JSON!")
                self.COUNT_Debug += 1
            if (self.FLAG_Debug == 2) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), " RETURN <-", self.MESSAGE_INCOMING)
                self.COUNT_Debug += 1
        if (method_name == 'send_message') and (self.FLAG_Debug != 0):
            if (self.FLAG_Debug == 1) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "[Запрос] Отправка сообщения в JSON. [Ответ] :",
                      response_send)
                self.COUNT_Debug += 1
            if (self.FLAG_Debug == 2) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), " RETURN <-", self.MESSAGE_SENT)
                self.COUNT_Debug += 1


oTrue = Bot("888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk")
oTrue.update_json()
oTrue.write_json()
oTrue.get_message(0)
oTrue.send_message(oTrue.get_message(-1)['chat_id'], "Привет")

print("------------Бесконечный------------")

'''
from time import sleep

while True:
    oTrue.update_json()
    sleep(2)
    if oTrue.get_message(-1)['text'] == "привет":
        oTrue.send_message(oTrue.get_message(-1)['chat_id'], "Вы начали работу!")

    if oTrue.get_message(-1)['text'] == "пока":
        pass
'''
