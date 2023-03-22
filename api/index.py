from flask import Flask, jsonify, render_template, request

from fetch_data import get_events_at_night
from logika import atlyginimo_skaiciuokle


app = Flask(__name__)


@app.route("/netto", methods=['GET', 'POST'])
def neto():
    if request.method == 'POST':
        atlyginimas_ant_popieriaus = request.form['atlyginimas']
        atskaiciuota = atlyginimo_skaiciuokle(float(atlyginimas_ant_popieriaus))
        return render_template('result_post.html', rezultatas=atskaiciuota)
    if request.method == "GET":
        gross = request.args.get('gross')
        atskaiciuota = atlyginimo_skaiciuokle(float(gross))
        return jsonify(atskaiciuota)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/moletu_observatorija')
def get_data():
    return jsonify(get_events_at_night())
