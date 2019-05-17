from flask import Flask, render_template, request, jsonify
from parsing import create_text, create_link, create_img
import Lesson07LawrParserNBRB

app = Flask(__name__)

link = create_link()
text = create_text()
img = create_img()

# 2019
parser = Lesson07LawrParserNBRB.LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
data = parser.update_json()[0]['Date'][0:10].replace("-", "")  # Имеет вид: 20190507
global year, month, day
year = int(data[0:4])
month = data[4:6]
day = data[6:9]
del parser  # Удаляем объект (так как в цикле он будет создаваться заново)




def gtt(y):
    # Создаем объект с курсами валют на определенную дату
    rates = Lesson07LawrParserNBRB.LawrParserNBRB(
        "http://www.nbrb.by/API/ExRates/Rates?onDate={}-{}-{}&Periodicity=0".format(y, month, day))
    rates.update_json()
    table = rates.get_table()
    del rates  # Удаляем объект (так как в цикле он будет создаваться заново)
    return table




@app.route('/', methods=['POST', 'GET'])  # вызываеться всегда когда на приложение поступает POST или GET
def index():
    if request.method == 'POST':  # Запрос от телеграмм на запись
        y = request.form['year']
        table = gtt(y)
        return render_template('index.html', TABLE=table, TEXT=text, IMG=img, LINK=link)
    if request.method == 'GET':  # Запрос на чтение (к примеру при обновлении страницы Flask)
        table = gtt(year)
        return render_template('index.html', TABLE=table, TEXT=text, IMG=img, LINK=link)


if __name__ == '__main__':
    app.run()
