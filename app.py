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

@app.route('/reclamarchun')
def reclamarchun():
    return render_template('reclamarchun.html')

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
    from flask import Flask, render_template, jsonify, request
import time

app = Flask(_name_)

# Simulamos almacenamiento en memoria (esto se perderá si la app se reinicia)
ultimos_reclamos = {}

# Datos de la billetera y API (ajusta según tu blockchain)
BILLETERA_ORIGEN = "0x6b2bA4159916017267c39A3b70b507F7c1Af5eDb"
TIEMPO_ESPERA = 24 * 60 * 60  # 24 horas en segundos

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reclamar', methods=['POST'])
def reclamar():
    usuario_id = request.remote_addr  # Usa la IP como identificador (mejor usar WLD ID)
    
    # Verifica si el usuario ya reclamó en las últimas 24 horas
    ahora = time.time()
    if usuario_id in ultimos_reclamos and (ahora - ultimos_reclamos[usuario_id] < TIEMPO_ESPERA):
        return jsonify({"mensaje": "Debes esperar 24 horas antes de reclamar nuevamente."}), 400

    # Actualiza el último reclamo del usuario
    ultimos_reclamos[usuario_id] = ahora

    # Simula la transferencia de tokens (ajusta según tu contrato inteligente)
    resultado = transferir_chun(BILLETERA_ORIGEN, usuario_id, 1000)

    if resultado:
        return jsonify({"mensaje": "¡1,000 CHUN enviados a tu billetera!"})
    else:
        return jsonify({"mensaje": "Error al procesar la transacción."}), 400

def transferir_chun(origen, destino, cantidad):
    """
    Aquí iría la lógica real para enviar CHUN desde el contrato en blockchain.
    Puede ser con web3.py, TronWeb, u otra API de tu red.
    """
    print(f"✅ Transfiriendo {cantidad} CHUN desde {origen} a {destino}...")
    return True  # Simula una transacción exitosa

if _name_ == '_main_':
    app.run(debug=True)
