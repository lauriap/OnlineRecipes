from application import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    timeNeeded = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.String(1000), nullable=False)


    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    recipeIngredients = db.relationship("RecipeIngredient", backref = "Recipe", lazy=True)

    def __init__(self, name, timeNeeded, instructions):
        self.name = name
        self.timeNeeded = timeNeeded
        self.instructions = instructions

class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.String(144), nullable=False)

    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)

    def __init__(self, amount):
        self.amount = amount
