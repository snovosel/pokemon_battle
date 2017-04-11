from flask import jsonify
from random import randint
from pokemon import app, db
from pokemon.models import Pokemon, Move
import pykemon
import random



def get_info():

    #don't forget to add the caching to this otherwise you will run out of requests

    pokemon = pykemon.get(pokemon_id=1)
    opponent = pykemon.get(pokemon_id=33)
    final = {'pokemon': {'moves': random.sample([{k:v} for k,v in pokemon.moves.iteritems()], 10), 'name': pokemon.name, 'hp': 100 }, 'opponent': {'moves': random.sample([{k:v} for k,v in opponent.moves.iteritems()], 10), 'name': opponent.name, 'hp': 100 } }
    return final


    '''db.session.add(moves=final['moves'], name=final['name'], hp=final['hp'])
    db.session.commit()

def get_move(move):
    move_get = pykemon.get(move_id=move)

    return move_get'''



def serialize_moves():
    return dict(name=move.name, url=move.url, pokemon_id=move.pokemon_id)
