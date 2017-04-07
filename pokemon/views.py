from flask import render_template, jsonify, json
from pokemon import app
from pokemon.utils import get_info
import requests


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/poke', methods=['GET'])
def index():
    return get_info()
