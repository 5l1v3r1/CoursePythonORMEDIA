# Класс бота, который работает используя requests (запросы в getupdates)
class LawrBotGetUpdates:
    # И Н Ф О Р М А Ц И Я
    # Получать обновления от телеграм можно через: 1) getupdates 2) Webhook
    #    1) Если "getupdates" - то работаем просто через [requests.post / requests.get]
    #    2) Если "Webhook"    - то работаем через [Django / Flask]
    # Работать с Flask можно через: 1) localhost 2) Тунель HTTP (localhost.run) 2) Тунель HTTPS (ngrok.com)

    # А Т Р И Б У Т Ы
    FLAG_Debug = 3  # =0..3 (Режимы)
    COUNT_Debug = 1  # Счетчик сообщений от debugging
    JSON = None  # Ответ от бота в JSON формате (все сообщения пользователя)
    FILE_JSON = None  # Объект открытого файла Lesson07(ClassWork).json
    MESSAGE_INCOMING = None  # Сообщение Входящее
    MESSAGE_SENT = None  # Сообщение Отправленное
    FLAG_SEND = False  # Флаг отслеживающий нужно ли отвечать боту на последнее сообщение (или уже ответил)
    PRE_APDATE_ID = None  # Содержит в себе update_id предпоследнего сообщения.

    # Инициализаци/создание бота
    def __init__(self, token):
        import requests
        self.TOKEN = token
        self.URL = "https://api.telegram.org/bot" + token + "/"
        requests.get(self.URL + 'setWebhook')  # Webhook is already deleted
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
    def write_json(self, filename='Lesson07(HomeWork).json'):
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
        # Вытягивем из JSON данные относящиеся к сообщению под номером "number"
        update_id = self.JSON['result'][number]['update_id']
        chat_id = self.JSON['result'][number]['message']['chat']['id']
        date = self.JSON['result'][number]['message']['date']
        text = self.JSON['result'][number]['message']['text']
        # Формируем словарь на основе вытянутых данных
        self.MESSAGE_INCOMING = {'chat_id': chat_id, 'update_id': update_id, 'date': date, 'text': text}
        # Проверяем и выставляем "FLAG_SEND"
        self.check_flag_update_id()
        self.debugging('get_message')
        return self.MESSAGE_INCOMING

    # ОТПРАВЛЯТЬ Сообщения
    def send_message(self, chat_id, text):
        import requests
        if self.FLAG_SEND:
            global response_send
            # 1 ВАРИАНТ - POST (Проблемы с отображением русских символов)
            # self.MESSAGE_SENT = {'chat_id': chat_id, 'text': text}
            # response_send = requests.post(self.URL + 'sendmessage', json=self.MESSAGE_SENT)
            # 2 ВАРИАНТ - GET (Проблем нет)
            response_send = requests.get(self.URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text))
            self.debugging('send_message')
            return self.MESSAGE_SENT

    # Отладка (отображает сообщения консоли и возвраты функций)
    def debugging(self, method_name):
        if (method_name == '__init__') and (self.FLAG_Debug != 0):
            if (self.FLAG_Debug == 1) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "Объект создан!")
                self.COUNT_Debug += 1
        if (method_name == 'update_json') and (self.FLAG_Debug != 0):
            if (self.FLAG_Debug == 1) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "Обновлен/Получен новый JSON. [Ответ] :",
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
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "Сообщение №", n,
                      "вытянуто из JSON! Флаг ответа:", self.FLAG_SEND)
                self.COUNT_Debug += 1
            if (self.FLAG_Debug == 2) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), " RETURN <-", self.MESSAGE_INCOMING)
                self.COUNT_Debug += 1
        if (method_name == 'send_message') and (self.FLAG_Debug != 0):
            if (self.FLAG_Debug == 1) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), "Консоль ->", "Отправка сообщения в JSON.   [Ответ] :",
                      response_send)
                self.COUNT_Debug += 1
            if (self.FLAG_Debug == 2) or (self.FLAG_Debug == 3):
                print("{0:0>3}".format(self.COUNT_Debug), " RETURN <-", self.MESSAGE_SENT)
                self.COUNT_Debug += 1

    # Проверка и сравнение pre_update_id и update_id, и выставление флага.
    def check_flag_update_id(self):
        if self.MESSAGE_INCOMING['update_id'] == self.PRE_APDATE_ID:  # Если текущий = предыдыдущему
            self.FLAG_SEND = False  # (Отвечать не нужно)
        if self.MESSAGE_INCOMING['update_id'] != self.PRE_APDATE_ID:  # Если текущий != предыдыдущему
            self.FLAG_SEND = True  # (Отвечать нужно)
        self.PRE_APDATE_ID = self.MESSAGE_INCOMING['update_id']
