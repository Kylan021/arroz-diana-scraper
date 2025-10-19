import json
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde React

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hola desde Flask!"})

@app.route("/api/historico", methods=["GET"])
def get_historico():
    with open(r"c:\Users\juesp\Documents\codes\ejercicios\electiva\diana prueva\arroz-diana-scraper\backend\database\Historico.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)