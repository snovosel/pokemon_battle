from flask import render_template, jsonify, json
from pokemon import app, db
from pokemon.models import Pokemon, Move
from pokemon.utils import get_info


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET'])
def index():
    data = get_info()
    return jsonify(data)

@app.route('/move/<int:x>', methods=['GET'])
def move_json(x):
    data = get_move(x)
    return jsonify(data)
