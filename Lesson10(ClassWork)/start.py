from flask import Flask, render_template
from parsing import create_text, create_link, create_img
import Lesson07LawrParserNBRB

app = Flask(__name__)

parser = Lesson07LawrParserNBRB.LawrParserNBRB("http://www.nbrb.by/API/ExRates/Rates?Periodicity=0")
parser.update_json()
table = parser.get_table()


@app.route('/')
def index():
    link = create_link()
    text = create_text()
    img = create_img()
    return render_template('index.html', TABLE=table, T=text, I=img, L=link)


@app.route('/hell')
def hell():
    return table


if __name__ == '__main__':
    app.run()
