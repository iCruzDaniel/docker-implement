from flask import Flask, request, jsonify
from flask_cors import CORS  # ← importa flask-cors
import os

app = Flask(__name__)
CORS(app)  # ← habilita CORS para todas las rutas

@app.route('/')
def hello():
    return 'Hola Docker'

@app.route('/mensaje', methods=['POST'])
def guardar_mensaje():
    data = request.get_json()
    mensaje = data.get('mensaje', '')
    
    if not mensaje:
        return jsonify({"error": "No se proporcionó mensaje"}), 400
    
    try:
        with open('/data/mensajes.txt', 'a') as f:
            f.write(mensaje + '\n')
        return jsonify({"status": "Mensaje guardado"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    os.makedirs('/data', exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
