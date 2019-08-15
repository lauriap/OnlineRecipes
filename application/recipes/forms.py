from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.ingredients.models import Ingredient
from application.recipes.models import Recipe

def ingredient_query():
    return Ingredient.query

def recipe_query():
    return Recipe.query

class RecipeForm(FlaskForm):
    name = StringField("Recipe name", [validators.Length(min=1)])
    timeNeeded = IntegerField("Time needed", [validators.NumberRange(min=1)])
    instructions = TextAreaField("Instructions", [validators.Length(min=1)])

    ingredient_1 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=False)
    quantity_1 = StringField("Quantity (e.g. 3 spoonfuls)", [validators.DataRequired()])

    ingredient_2 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_2 = StringField("Quantity", [validators.Optional()])

    ingredient_3 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_3 = StringField("Quantity", [validators.Optional()])

    ingredient_4 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_4 = StringField("Quantity", [validators.Optional()])

    ingredient_5 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_5 = StringField("Quantity", [validators.Optional()])

    ingredient_6 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_6 = StringField("Quantity", [validators.Optional()])

    ingredient_7 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_7 = StringField("Quantity", [validators.Optional()])

    ingredient_8 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_8 = StringField("Quantity", [validators.Optional()])

    ingredient_9 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_9 = StringField("Quantity", [validators.Optional()])

    ingredient_10 = QuerySelectField(query_factory=ingredient_query, get_label="name", allow_blank=True)
    quantity_10 = StringField("Quantity", [validators.Optional()])


    class Meta:
        csrf = False


class DeleteForm(FlaskForm):
   # id = IntegerField("Recipe number", [validators.NumberRange(min=1, message="Please select a recipe number from the list below.")])
    id = QuerySelectField(query_factory=recipe_query, get_label="id", allow_blank=True)

    class Meta:
        csrf = False

class UpdateForm(FlaskForm):
    id = IntegerField("Recipe number", [validators.NumberRange(min=1, message="Please select a recipe number from the list below.")])
    name = StringField("New recipe name", [validators.Optional()])
    timeNeeded = IntegerField("New time", [validators.Optional()])
    instructions = StringField("New instructions", [validators.Optional()])

    class Meta:
        csrf = False

