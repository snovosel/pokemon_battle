from flask import jsonify
from random import randint
from pokemon import app, db
from pokemon.classes import Pokemon, Move
import pykemon
import requests
import random

p = random.randint(0, 100)
o = random.randint(0, 100)
pokemon = Pokemon(1)
opponent = Pokemon(47)


def initialize_fight():
    return dict(pokemon=pokemon.to_dict(), opponent=opponent.to_dict())


def pokemon_attack(move):
    opponent.hp -= pokemon.attack(15)
    return dict(pokemon=pokemon.to_dict(), opponent=opponent.to_dict())













'''def attack(move, pokemon):
    final = Pokemon.hp - move.power
    return final'''


#flow ---- all hp,name,moves go to index(json)
#          move is pressed, id is sent to server
#          move power is subtracted from hp
#          all hp, name, moves go to index
