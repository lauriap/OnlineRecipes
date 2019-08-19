from application import db
from application.ingredients.models import Ingredient

from sqlalchemy.sql import text

class Recipe(db.Model):
    __tablename__ = "recipe"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    timeNeeded = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.String(1000), nullable=False)


    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    account = db.relationship("User", back_populates="recipes")

    recipeIngredients = db.relationship("RecipeIngredient", back_populates="recipe", lazy="joined")

    def __init__(self, name, timeNeeded, instructions):
        self.name = name
        self.timeNeeded = timeNeeded
        self.instructions = instructions

    def get_id(self):
        return self.id



class RecipeIngredient(db.Model):
    __tablename__ = "recipe_ingredient"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(144), nullable=False)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)

    recipe = db.relationship("Recipe", back_populates="recipeIngredients")
    ingredient = db.relationship("Ingredient", back_populates="recipeIngredients")

    def __init__(self, amount):
        self.amount = amount


