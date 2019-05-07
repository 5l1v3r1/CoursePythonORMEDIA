# Класс отвечающий за парсинг/отображение/вывод валют
class LawrParserNBRB:
    JSON = None  # Ответ от сайта в JSON формате (все курсы валют)
    FILE_JSON = None  # Объект открытого файла Lesson07(ClassWork).json

    # Инициализаци/создание парсера
    def __init__(self, URL):
        self.URL = URL

    # Получить JSON
    def update_json(self):
        import requests
        self.JSON = requests.get(self.URL).json()
        return self.JSON

    # ЗАПИСАТЬ JSON В ФАЙЛ (с форматирование)
    def write_json(self, filename='Lesson07(HomeWork).json'):
        import json
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
