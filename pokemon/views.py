from flask import render_template, jsonify, json, request
from pokemon import app, db
from pokemon.models import Pokemon, Move
from pokemon.utils import initialize_fight, pokemon_attack
from pokemon.classes import Pokemon, Move
import urlparse


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pokemon', methods=['GET'])
def index():
    data = initialize_fight()
    return jsonify(data)


@app.route('/move/', methods=['GET', 'POST'])
def move_json():
    move = request.args.get('move_id')
    name = request.args.get('name')

    return jsonify(pokemon_attack(move))
