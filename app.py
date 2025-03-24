from flask import Flask, render_template, redirect, url_for, request, jsonify
import requests

app = Flask(__name__)

WORLDCOIN_VERIFY_URL = "https://developer.worldcoin.org/api/v1/verify"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')

@app.route('/next-page')
def next_page():
    return render_template('next_page.html')  # O cualquier otra página que desees

@app.route('/wdd')
def wdd():
    return render_template('wdd.html')  # Asegúrate de que este archivo está en la carpeta templates

@app.route('/buscador')
def buscador():
    return render_template('buscador.html')

@app.route('/api/verify', methods=['POST'])
def verify_proof():
    # Se reciben los datos del frontend para verificar el World ID
    data = request.json

    # Hacer la solicitud POST a la API de Worldcoin para la verificación
    response = requests.post(WORLDCOIN_VERIFY_URL, json=data)

    # Devolver la respuesta de la API al frontend
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
