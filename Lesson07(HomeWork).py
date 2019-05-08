import Lesson07LawrParserNBRB

# ------------------------------ GETAPDATE. ОСНОВНОЙ КОД main ------------------------------
'''
import Lesson07LawrBotGetUpdates
from time import sleep

# Создание Объектов
oTrue = Lesson07LawrBotGetUpdates.LawrBotGetUpdates("888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk")
rates = Lesson07LawrParserNBRB.LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
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

import Lesson07LawrBotWebhook

# Создание объектов
rates = Lesson07LawrParserNBRB.LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
oTrue = Lesson07LawrBotWebhook.LawrBotWebhook("888175405:AAGnCJ-dGyToTh3lGaa-D716cjLKtZVTgAk",
                                              "https://lawr.localhost.run")
oTrue.creation_flask(rates)  # Запуск приложения Flask (уже с нужным функционалом)
app = oTrue.APP  # Flask-у на хостинге проще работать с обычной переменной "app"

if __name__ == '__main__':
    app.run()  # Запускаем объект "app"="oTrue.APP" (приложение фласка)
