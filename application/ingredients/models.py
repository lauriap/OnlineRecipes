
from application import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)

    recipeIngredients = db.relationship("RecipeIngredient", backref="Ingredient", lazy=True)

    def __init__(self, name):
        self.name = name


