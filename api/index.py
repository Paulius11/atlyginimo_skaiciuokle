from flask import Flask, render_template, request

from logika import atlyginimo_skaiciuokle

app = Flask(__name__)


@app.route("/netto", methods=['GET', 'POST'])
def neto():
    if request.method == 'POST':
        atlyginimas_ant_popieriaus = request.form['atlyginimas']
        atskaiciuota = atlyginimo_skaiciuokle(int(atlyginimas_ant_popieriaus))
        return render_template('rezultatas.html', rezultatas=atskaiciuota)


@app.route("/")
def hello_world():
    return render_template('index.html')
