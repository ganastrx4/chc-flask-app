from flask import Flask, request, jsonify
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Por si necesitas aceptar peticiones externas

@app.route('/guardar-verificacion', methods=['POST'])
def guardar_verificacion():
    data = request.get_json()
    print("✅ Datos recibidos desde World ID:", data)

    # Aquí puedes guardar el usuario en la base de datos, marcarlo como verificado, etc.
    
    return jsonify({"status": "ok"})


@app.route('/api/verify', methods=['POST'])
def verify_world_id():
    # Obtener el 'world_id' y 'proof' desde el cuerpo de la solicitud
    data = request.get_json()
    world_id = data.get('world_id')
    proof = data.get('proof')

    if not world_id or not proof:
        return jsonify({"success": False, "message": "Datos incompletos"}), 400

    # Realizar la solicitud a la API de Worldcoin para verificar el 'world_id' y el 'proof'
    response = requests.post('https://id.worldcoin.org/verify', json={
        "world_id": world_id,
        "proof": proof,
        "action_id": "app_7686f9027d3e3c0b53d987a3caf1e111",  # Asegúrate de usar tu Action ID
        "signal": "user_login"
    })

    # Procesar la respuesta de la API de Worldcoin
    result = response.json()

    if result.get('success'):
        return jsonify({"success": True, "message": "Usuario verificado con éxito"}), 200
    else:
        return jsonify({"success": False, "message": result.get('message', 'Error en la verificación')}), 400

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/wdd.html')
def wdd():
    return render_template('wdd.html')  # Asegúrate de que este archivo está en la carpeta templates

@app.route('/bienvenida')
def bienvenida():
    return render_template('bienvenida.html')

@app.route('/salas')
def next_page():
    return render_template('salas.html')  # O cualquier otra página que desees
if __name__ == '__main__':
    app.run(debug=True)
