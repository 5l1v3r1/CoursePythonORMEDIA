from flask import Flask, render_template, request
from parsing import create_text, create_link, create_img
import Lesson07LawrParserNBRB


# Возвращает текущую дату в формате [год, месяц, день]
def date_now():
    parser = Lesson07LawrParserNBRB.LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
    data = parser.update_json()[0]['Date'][0:10].replace("-", "")  # Имеет вид: 20190507
    year = int(data[0:4])
    month = data[4:6]
    day = data[6:9]
    del parser
    data = [year, month, day]
    return data


# Возвращает таблицу в формате [{валюта1}, {валюта2}..]
def create_table(year, month, day):
    rates = Lesson07LawrParserNBRB.LawrParserNBRB(
        "http://www.nbrb.by/API/ExRates/Rates?onDate={}-{}-{}&Periodicity=0".format(year, month, day))
    rates.update_json()
    table = rates.get_table()
    del rates
    print(table)
    return table


# Возвращает афишу в формате [[текст1, текст2..], [ссылка1, ссылка2..], [img1, img2..]]
def create_afisha():
    text = create_text()
    link = create_link()
    img = create_img()
    afisha = [text, link, img]
    return afisha


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':  # Отправить данные в HTML
        form_year = request.form['year']
        afisha = create_afisha()
        table = create_table(form_year, date_now()[1], date_now()[2])
        return render_template('index.html', TABLE=table, AFISHA=afisha, YEAR=form_year)
    if request.method == 'GET':  # Запрос на чтение (к примеру при обновлении страницы Flask)
        afisha = create_afisha()
        table = create_table(date_now()[0], date_now()[1], date_now()[2])
        return render_template('index.html', TABLE=table, AFISHA=afisha, YEAR=date_now()[0])


if __name__ == '__main__':
    app.run()
