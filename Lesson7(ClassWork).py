print("-------------------------------------------- Создание бота в Telegram. BotFather.")

# Заготовка / Шаблон # https://api.telegram.org/botТОКЕН/GetUpdates
# Мой токен (приходит от BotFather) # 888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk
# Заготовка + Мой токен # https://api.telegram.org/bot888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk/GetUpdates

print("-------------------------------------------- Написание кода для бота в Telegram. Писать/Читать")

TOKEN = "888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk"
URL = "https://api.telegram.org/bot" + TOKEN + "/"


# Проверить работает ли бот (Ответ: Response [200])
def get_bot_check():
    import requests
    result = requests.get(URL + "getupdates")
    return result


# Обновить/Получить JSON
def get_updates():
    import requests
    result = requests.get(URL + "getupdates")
    return result.json()


# ПОЛУЧАТЬ Сообщения
def get_message():
    data = get_updates()
    chat_id = data['result'][-1]['message']['chat']['id']
    text = data['result'][-1]['message']['text']
    result = {'chat_id': chat_id, 'text': text}
    return result


# ОТПРАВЛЯТЬ Сообщения
def send_message(chat_id, text):
    import requests
    result = requests.get(URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text))
    return result
    # return "Сообщение отправленно"


'''
print(get_bot_check())
print(get_updates())
print(get_message())
'''
print(send_message(get_message()['chat_id'], "Что тебе нужно?"))

print("-------------------------------------------- Красивый вид JSON (запись в файл)")


def write_json(data, filename='Lesson7(ClassWork).json'):
    import json
    # Создаем object_filename(открытый для записи файловый объект) привязанный к файлу "filename"
    with open(filename, 'w') as object_filename:
        # Метод который записывает в object_filename(файловый объект) данные JSON
        json.dump(data, object_filename, indent=2, ensure_ascii=False)  # Два последних параметра для красоты вывода


write_json(get_updates())

print("-------------------------------------------- Обработка ответов.")


def main():
    while True:
        answer = get_message()
        if 'ничего' in answer['text']:
            send_message(answer['chat_id'], 'тогда проваливай!')
            break


if __name__ == '__main__':
    main()
