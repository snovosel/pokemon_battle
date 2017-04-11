from pokemon import db


class Pokemon(db.Model):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    name= db.Column(db.String(64), index=True, unique=False)
    hp= db.Column(db.Integer, index=True, default=100)
    moves = db.relationship('Move', backref='Pokemon', lazy='dynamic')

    def __init__(self, name, hp, moves):
        self.name = name
        self.hp = hp
        self.moves = moves

    def to_dict(self):
        return dict(id= self.id, name= self.name, hp= self.hp, moves= self.moves)

class Move(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    url= db.Column(db.String())
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))


    def to_dict(self):
        return dict(id= self.id, name= self.name, url= self.url, pokemon_id= self.pokemon_id)
