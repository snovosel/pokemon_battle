from flask import jsonify
from pokemon import app
import requests

def get_info():
    # retrieve full API information for user's pokemon and opponent (random integers will be used in production)

    my_poke = requests.get('https://pokeapi.co/api/v2/pokemon/1').json()
    opponent = requests.get('https://pokeapi.co/api/v2/pokemon/72').json()

    #retrieve name, 3 moves

    fight_info = [  {key: move['move'][key] for key in move['move']} for move in my_poke.get('moves')[0:3], {key: move['move'][key] for key in move['move']} for move in opponent.get('moves')[0:3] ]

    fight_info.append(my_poke.get('name'))

    return jsonify(fight_info)
