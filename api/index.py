from flask import Flask, jsonify, render_template, request
import requests
from logika import atlyginimo_skaiciuokle

app = Flask(__name__)


@app.route("/netto", methods=['GET', 'POST'])
def neto():
    if request.method == 'POST':
        atlyginimas_ant_popieriaus = request.form['atlyginimas']
        atskaiciuota = atlyginimo_skaiciuokle(int(atlyginimas_ant_popieriaus))
        return render_template('rezultatas.html', rezultatas=atskaiciuota)
    if request.method == "GET":
        gross = request.args.get('gross')
        atskaiciuota = atlyginimo_skaiciuokle(int(gross))
        return jsonify(atskaiciuota)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    gross = request.args.get('gross')
    data = {'message': 'Hello world!', 'gross': gross}
    return jsonify(data)
