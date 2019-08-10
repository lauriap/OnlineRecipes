
from application import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

#    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
 #                          nullable=False)

    def __init__(self, name):
        self.name = name


