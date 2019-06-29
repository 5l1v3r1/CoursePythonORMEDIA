from ClassLawr_MongoDB import MongoDB
import Lesson07LawrParserNBRB
from selenium import webdriver
from time import sleep
import os

print("-------------------------------------------- Задание 1 (67)")

'''
Создать бд с данными о курсах валют за последние 20 лет (Немного поменял условие, уж очень было интересно).
'''

# Создание объекта Базы данных
string = "localhost:27017"
BD = MongoDB(connection_string=string, ssl=False)

# Получаем такущую дату (можно было проще, но сделал через свой класс, что был под рукой)
rates = Lesson07LawrParserNBRB.LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
data = rates.update_json()[0]['Date'][0:10].replace("-", "")  # Имеет вид: 20190507
del rates

# Разбиваем дату на переменные для удобства
year = int(data[0:4])
month = data[4:6]
day = data[6:9]

for i in range(20 + 1):  # Цикл от 0 до 20
    # Формируем название таблицы на основе даты
    name_collection = 'rates' + str(year - i) + str(month) + str(day)
    # Создаем таблицу (Если уже есть, то перезапись)
    BD.delete_collection('Lesson13(HomeWork)', name_collection)
    # Создаем объект с курсами валют на определенную дату
    rates = Lesson07LawrParserNBRB.LawrParserNBRB(
        "http://www.nbrb.by/API/ExRates/Rates?onDate={}-{}-{}&Periodicity=0".format(year - i, month, day))

    # Заполненяем таблицу объектом (с курсами валют)
    for line in rates.update_json():  # Цикл по линиям (словарям) c 1-ой валюты по последнюю
        BD.add_line_to_end('Lesson13(HomeWork)', name_collection, {'Cur_Abbreviation': line['Cur_Abbreviation'],
                                                       'Cur_Name': line['Cur_Name'],
                                                       'Cur_Scale': line['Cur_Scale'],
                                                       'Cur_OfficialRate': line['Cur_OfficialRate']})
    BD.nice_print(BD.show_collection('Lesson13(HomeWork)', name_collection))

    del rates  # Удаляем объект (так как в цикле он будет создаваться заново)

print("-------------------------------------------- Задание 2 (86)")

'''
Написать бота для сайта знакомств "Badoo" при помощи Selenium, 
который бы имитировал действия пользователя (ставил сердечки или кресты)
https://www.youtube.com/watch?v=FKwbxMP8yko&feature=youtu.be
'''

# Задание путей
executable_path = "driver_chrome/chromedriver_mac64"
browser = webdriver.Chrome(executable_path=executable_path)
# --АВТОРИЗАЦИЯ--
browser.get("https://badoo.com/ru/signin/")
textarea = browser.find_element_by_name('email')
textarea.send_keys('interes46@mail.ru')
textarea = browser.find_element_by_name('password')
textarea.send_keys('lydaruqa')
submit = browser.find_element_by_name('post')
submit.click()
# --ДЕЙСТВИЯ лайк/дизлайк--
sleep(10)
flag = True
for i in range(5):
    sleep(4)  # увеличить при ошибке (попробывать лайк в ручную)
    # css_selector = .xxx (на примере: class="xxx yyy zzz")
    if flag:
        submit = browser.find_element_by_css_selector('.profile-action--yes')
        flag = False
    else:
        submit = browser.find_element_by_css_selector('.js-profile-header-vote-no')
        flag = True
    submit.click()
browser.quit()
os.remove("geckodriver.log")  # Удаление файла "geckodriver.log"


