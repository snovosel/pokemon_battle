from flask import jsonify
from random import randint
from pokemon import app, db
from pokemon.classes import Pokemon, Move
import pykemon
import requests
import random

p = random.randint(0, 100)
o = random.randint(0, 100)
pokemon = Pokemon(p)
opponent = Pokemon(o)


def initialize_fight():
    return dict(pokemon=pokemon.to_dict(), opponent=opponent.to_dict())


def pokemon_attack(name, move):



    if name == 'pokemon':
        opponent.hp -= pokemon.attack(move)
        return dict(pokemon=pokemon.to_dict(), opponent=opponent.to_dict())
    elif name == 'opponent':
        pokemon.hp -= opponent.attack(15)
        return dict(pokemon=pokemon.to_dict(), opponent=opponent.to_dict())
