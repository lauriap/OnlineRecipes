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

    @staticmethod
    def get_recipe_count():
        stmt = text("SELECT COUNT(Recipe.id) FROM Recipe;")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"count":row[0]})

        count = response[0].get("count")
        return count

    @staticmethod
    def get_most_used_ingredient():
        stmt = text("SELECT Ingredient.name, COUNT(Recipe_Ingredient.id) FROM Ingredient"
                    " LEFT JOIN Recipe_Ingredient ON Ingredient.id = Recipe_Ingredient.ingredient_id"
                    " GROUP BY ingredient.name;")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0], "uses":row[1]})

        most_used_ing_name = response[0].get("name")
        return response

    @staticmethod
    def list_top_contributors():
        stmt = text("SELECT Account.id, Account.name, COUNT(Recipe.id) FROM Account"
                    " LEFT JOIN Recipe ON Recipe.account_id = Account.id"
                    " GROUP BY account.id, account.name;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[1], "recipecount":row[2]})

        return response




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

    def get_ingredient_id(self):
        return self.ingredient_id

    def set_ingredient_id(self, id):
        self.id = id
