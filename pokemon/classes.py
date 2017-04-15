from flask import jsonify
from random import randint
from pokemon import app, db
from pokemon.models import Pokemon, Move
import pykemon
import requests
import random

class Pokemon(object):

    def __init__(self, num):

        pokemon = pykemon.get(pokemon_id=num)

        self.id = num
        self.name = pokemon.name
        self.hp = 1000
        self.moves = random.sample([{k:v} for k,v in pokemon.moves.iteritems()], 10)

    def to_dict(self):
        return dict(id=self.id, name=self.name, hp=self.hp, moves=self.moves)

    def attack(self, move_id):
        move = Move(move_id)
        print move.power
        return move.power



class Move(object):
    def __init__(self, move_id):

        move = pykemon.get(move_id=move_id)
        self.id = move_id
        self.name = move.name
        self.power = move.power

    def to_dict(self):
        return dict(id=self.id, name=self.name, power=self.power)
