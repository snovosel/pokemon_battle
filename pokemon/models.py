from pokemon import db


class Pokemon(db.Model):
    id= db.Column(db.Integer, primary_key=True, autoincrement=True)
    name= db.Column(db.String(64), index=True, unique=False)
    hp= db.Column(db.Integer, index=True, default=100)


    def to_dict(name, hp):
        return dict(id= self.id, name= self.name, hp= self.hp)

    def use_move(move):
        move = Move.query.get_or_404(move)
        result_hp = self.hp - move.power

        return to_dict(move.name, result_hp)

class Move(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String())
    power = db.Column(db.Integer, default=0)

    def __init__(self, name, power):
        self.name = name
        self.power = power


    def to_dict(self):
        return dict(id= self.id, name= self.name, power= self.power)







#the idea here is that moves and pokemon are separate entities, each with their own attributes
# attributes/specialties/etc.. It's the combination of these attributes which make for more
# possibilities ingame and also the ability to come and go.
