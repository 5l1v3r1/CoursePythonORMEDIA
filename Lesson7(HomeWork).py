import json
import requests
from flask import Flask
from flask import request, jsonify


# Класс бота, который работает используя requests (запросы в getupdates)
class BotGetUpdates:
    # Получать обновления от телеграм можно через: 1) getupdates 2) Webhook
    #    1) Если "getupdates" - то работаем просто через [requests.post / requests.get]
    #    2) Если "Webhook"    - то работаем через [Django / Flask]
    # Работать с Flask можно через: 1) localhost 2) Тунель HTTP (localhost.run) 2) Тунель HTTPS (ngrok.com)

    # Атрибуты класса
    FLAG_Debug = 3  # =0..3 (Режимы)
    COUNT_Debug = 1  # Счетчик сообщений от debugging
    JSON = None  # Ответ от бота в JSON формате (все сообщения пользователя)
    FILE_JSON = None  # Объект открытого файла Lesson7(ClassWork).json
    MESSAGE_INCOMING = None  # Сообщение Входящее
    MESSAGE_SENT = None  # Сообщение Отправленное
    FLAG_SEND = False  # Флаг отслеживающий нужно ли отвечать боту на последнее сообщение (или уже ответил)
    PRE_APDATE_ID = None  # Содержит в себе update_id предпоследнего сообщения.

    # Инициализаци/создание бота
    def __init__(self, token):
        self.TOKEN = token
        self.URL = "https://api.telegram.org/bot" + token + "/"
        requests.get(self.URL + 'setWebhook')  # Webhook is already deleted
        self.debugging('__init__')

    # ОБНОВИТЬ JSON
    def update_json(self):
        global response_update
        response_update = requests.get(self.URL + "getupdates")
        self.JSON = response_update.json()
        self.debugging('update_json')
        return self.JSON

    # ЗАПИСАТЬ JSON В ФАЙЛ (с форматирование)
    def write_json(self, filename='Lesson7(HomeWork).json'):
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


# Класс бота, который работает через API Telegram (Flask, Webhook)
class BotWebhook:
    # И Н Ф О Р М А Ц И Я
    # Получать обновления от телеграм можно через: 1) getupdates 2) Webhook
    #    1) Если "getupdates" - то работаем просто через [requests.post / requests.get]
    #    2) Если "Webhook"    - то работаем через [Django / Flask]
    # Работать с Flask можно через: 1) localhost 2) Тунель HTTP (localhost.run) 2) Тунель HTTPS (ngrok.com)

    # А Т Р И Б У Т Ы
    APP = None  # Приложение Flask
    JSON = None  # Ответ от бота в JSON формате (все сообщения пользователя)
    FILE_JSON = None  # Объект открытого файла Lesson7(ClassWork).json
    FLAG_SEND = False  # Флаг отслеживающий нужно ли отвечать боту на последнее сообщение (или уже ответил)
    MESSAGE_SENT = None  # Сообщение Отправленное
    MESSAGE_INCOMING = None  # Сообщение Входящее

    # Инициализаци/создание бота
    # https://api.telegram.org/bot888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk/setWebhook?url=https://lawr.localhost.run/
    def __init__(self, token, web_address):
        self.TOKEN = token
        self.URL = "https://api.telegram.org/bot" + token + "/"
        requests.get(self.URL + 'setWebhook?url=' + web_address)  # Webhook was set

    # Создание приложения Flask
    def creation_flask(self):
        self.APP = Flask(__name__)  # Создаем экземпляр "app" класса "Flask" (приложение фласка)
        self.creation_web()  # Создаем страицы сайта
        self.APP.run()  # Запускаем объект (приложение фласка)

    # Создание страницы для приложения Flask
    def creation_web(self):
        @self.APP.route('/', methods=['POST', 'GET'])  # вызываеться всегда когда на приложение поступает POST или GET
        def index():
            if request.method == 'POST':  # Запрос от телеграмм на запись
                self.JSON = request.get_json()
                self.write_json()
                self.get_message()
                self.send_message_rates()
                return jsonify(self.JSON)  # Для работы с POST нужно обязательно вернуть JSON объект (хз зачем и что)
            if request.method == 'GET':  # Запрос на чтение (к примеру при обновлении страницы Flask)
                return '<h1>Hello bot!</h1>'

    # ЗАПИСАТЬ JSON В ФАЙЛ (с форматирование)
    def write_json(self, filename='Lesson7(HomeWork).json'):
        # Создаем object_filename(открытый для записи файловый объект) привязанный к файлу "filename"
        with open(filename, 'w') as self.FILE_JSON:
            # Метод который записывает в object_filename(файловый объект) данные JSON
            json.dump(self.JSON, self.FILE_JSON, indent=2, ensure_ascii=False)

    # ПОЛУЧАТЬ Сообщения
    def get_message(self):
        # Вытягивем из JSON данные относящиеся к сообщению
        update_id = self.JSON['update_id']
        chat_id = self.JSON['message']['chat']['id']
        date = self.JSON['message']['date']
        text = self.JSON['message']['text']
        # Формируем словарь на основе вытянутых данных
        self.MESSAGE_INCOMING = {'chat_id': chat_id, 'update_id': update_id, 'date': date, 'text': text}

    # ОТПРАВЛЯТЬ Сообщения
    def send_message(self, chat_id, text, methods="POST"):
        import requests
        if methods == "POST":
            self.MESSAGE_SENT = {'chat_id': chat_id, 'text': text}
            requests.post(self.URL + 'sendmessage', json=self.MESSAGE_SENT)
        if methods == "GET":
            requests.get(self.URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text))

    # ОТПРАВЛЯТЬ Сообщения (Настроенно на вывод курсов валют)
    def send_message_rates(self):
        rates.update_json()
        # Отвечаем на последние сообщение
        if (self.MESSAGE_INCOMING['text'] == "/help") or (self.MESSAGE_INCOMING['text'] == "/start"):
            self.send_message(self.MESSAGE_INCOMING['chat_id'], rates.print_help())
        # Чтобы не писать много "if" генерируем основании списка полученного из rates.list_cur_abbreviation()
        for cur_abb in rates.list_cur_abbreviation():
            if self.MESSAGE_INCOMING['text'] == "/" + cur_abb.swapcase():
                self.send_message(self.MESSAGE_INCOMING['chat_id'], rates.print_money(rates.get_money(cur_abb)))


# ------------------------------ GETAPDATE. ОСНОВНОЙ КОД main ------------------------------
'''
# Создание Объектов
oTrue = BotGetUpdates("888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk")
rates = ParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
from time import sleep
while True:
    # Обновление Данных (первоначально данные все в JSON)
    rates.update_json()
    oTrue.update_json()
    oTrue.write_json()
    # Получаем последнее сообщение -> Формируем "self.MESSAGE_INCOMING"
    oTrue.get_message(-1)
    # Отвечаем на последние сообщение
    if (oTrue.MESSAGE_INCOMING['text'] == "/help") or (oTrue.MESSAGE_INCOMING['text'] == "/start"):
        oTrue.send_message(oTrue.MESSAGE_INCOMING['chat_id'], rates.print_help())
    # Чтобы не писать много "if" генерируем основании списка полученного из rates.list_cur_abbreviation()
    for cur_abb in rates.list_cur_abbreviation():
        if oTrue.MESSAGE_INCOMING['text'] == "/" + cur_abb.swapcase():
            oTrue.send_message(oTrue.MESSAGE_INCOMING['chat_id'], rates.print_money(rates.get_money(cur_abb)))
    print("-----------------------------------")
    sleep(1)
'''

# ------------------------------ WEBHOOK.   ОСНОВНОЙ КОД main ------------------------------

# 1) ПОСЛЕЗАПУСКА FLASK (это localhost) -> http://127.0.0.1:5000/ -> ДЕЛАЕМ ТУНЕЛЬ (для доступа из интернета)
# 2) ПИШЕМ В КОНСОЛЬ -> ssh -R 80:localhost:5000 ssh.localhost.run
# 3) НАШ FLASK ТЕПЕРЬ ДОСТУПЕН (это интернет адресс) -> https://lawr.localhost.run/

# Создание объектов
rates = ParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
oTrue = BotWebhook("888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk", "https://lawr6.localhost.run")
oTrue.creation_flask()  # Запуск приложения Flask (уже с нужным функционалом)
