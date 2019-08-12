from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=1)])
    timeNeeded = IntegerField("Time needed", [validators.NumberRange(min=1)])
    instructions = TextAreaField("Instructions", [validators.Length(min=1)])

    ingredient_name1 = StringField("Ingredient 1", [validators.Optional()])
    quantity1 = StringField("Quantity (e.g. 3 spoonfuls)", [validators.Optional()])

    ingredient_name2 = StringField("Ingredient 2", [validators.Optional()])
    quantity2 = StringField("Quantity", [validators.Optional()])

    ingredient_name3 = StringField("Ingredient 3", [validators.Optional()])
    quantity3 = StringField("Quantity", [validators.Optional()])

    ingredient_name4 = StringField("Ingredient 4", [validators.Optional()])
    quantity4 = StringField("Quantity", [validators.Optional()])

    ingredient_name5 = StringField("Ingredient 5", [validators.Optional()])
    quantity5 = StringField("Quantity", [validators.Optional()])

    ingredient_name6 = StringField("Ingredient 6", [validators.Optional()])
    quantity6 = StringField("Quantity", [validators.Optional()])

    ingredient_name7 = StringField("Ingredient 7", [validators.Optional()])
    quantity7 = StringField("Quantity", [validators.Optional()])

    ingredient_name8 = StringField("Ingredient 8", [validators.Optional()])
    quantity8 = StringField("Quantity", [validators.Optional()])

    ingredient_name9 = StringField("Ingredient 9", [validators.Optional()])
    quantity9 = StringField("Quantity", [validators.Optional()])

    ingredient_name10 = StringField("Ingredient 10", [validators.Optional()])
    quantity10 = StringField("Quantity", [validators.Optional()])



    class Meta:
        csrf = False


class DeleteForm(FlaskForm):
    id = IntegerField("Recipe number", [validators.NumberRange(min=1, message="Please select a recipe number from the list below.")])

    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    id = IntegerField("Recipe number", [validators.NumberRange(min=1, message="Please select a recipe number from the list below.")])
    name = StringField("New recipe name", [validators.Optional()])
    timeNeeded = IntegerField("New time", [validators.Optional()])
    instructions = StringField("New instructions", [validators.Optional()])

    class Meta:
        csrf = False

