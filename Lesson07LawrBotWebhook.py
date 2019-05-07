# Класс бота, который работает через API Telegram (Flask, Webhook)
class LawrBotWebhook:
    # И Н Ф О Р М А Ц И Я
    # Получать обновления от телеграм можно через: 1) getupdates 2) Webhook
    #    1) Если "getupdates" - то работаем просто через [requests.post / requests.get]
    #    2) Если "Webhook"    - то работаем через [Django / Flask]
    # Работать с Flask можно через: 1) localhost 2) Тунель HTTP (localhost.run) 2) Тунель HTTPS (ngrok.com)

    # А Т Р И Б У Т Ы
    APP = None  # Приложение Flask
    JSON = None  # Ответ от бота в JSON формате (все сообщения пользователя)
    FILE_JSON = None  # Объект открытого файла Lesson07(ClassWork).json
    FLAG_SEND = False  # Флаг отслеживающий нужно ли отвечать боту на последнее сообщение (или уже ответил)
    MESSAGE_SENT = None  # Сообщение Отправленное
    MESSAGE_INCOMING = None  # Сообщение Входящее

    # Инициализаци/создание бота
    # https://api.telegram.org/bot888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk/setWebhook?url=https://lawr.localhost.run/
    def __init__(self, token, web_address):
        import requests
        self.TOKEN = token
        self.URL = "https://api.telegram.org/bot" + token + "/"
        requests.get(self.URL + 'setWebhook?url=' + web_address)  # Webhook was set

    # Создание приложения Flask
    def creation_flask(self, object_parser):
        from flask import Flask
        self.APP = Flask(__name__)  # Создаем экземпляр "app" класса "Flask" (приложение фласка)
        self.creation_web(object_parser)  # Создаем страицы сайта
        self.APP.run()  # Запускаем объект (приложение фласка)

    # Создание страницы для приложения Flask
    def creation_web(self, object_parser):
        from flask import request, jsonify
        @self.APP.route('/', methods=['POST', 'GET'])  # вызываеться всегда когда на приложение поступает POST или GET
        def index():
            if request.method == 'POST':  # Запрос от телеграмм на запись
                self.JSON = request.get_json()
                self.write_json()
                self.get_message()
                self.send_message_rates(object_parser)
                return jsonify(self.JSON)  # Для работы с POST нужно обязательно вернуть JSON объект (хз зачем и что)
            if request.method == 'GET':  # Запрос на чтение (к примеру при обновлении страницы Flask)
                return '<h1>Hello bot!</h1>'

    # ЗАПИСАТЬ JSON В ФАЙЛ (с форматирование)
    def write_json(self, filename='Lesson07(HomeWork).json'):
        import json
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
    def send_message_rates(self, object_parser):
        object_parser.update_json()
        # Отвечаем на последние сообщение
        if (self.MESSAGE_INCOMING['text'] == "/help") or (self.MESSAGE_INCOMING['text'] == "/start"):
            self.send_message(self.MESSAGE_INCOMING['chat_id'], object_parser.print_help())
        # Чтобы не писать много "if" генерируем основании списка полученного из rates.list_cur_abbreviation()
        for cur_abb in object_parser.list_cur_abbreviation():
            if self.MESSAGE_INCOMING['text'] == "/" + cur_abb.swapcase():
                self.send_message(self.MESSAGE_INCOMING['chat_id'],
                                  object_parser.print_money(object_parser.get_money(cur_abb)))
