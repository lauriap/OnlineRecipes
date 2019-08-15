from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application.ingredients.models import Ingredient

def ingredient_query():
    return Ingredient.query

class IngredientForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=1)])

    class Meta:
        csrf = False


class DeleteIngredientForm(FlaskForm):
    #id = IntegerField("Ingredient number", [validators.NumberRange(min=1, message="Please select an ingredient number from the list below.")])
    id = QuerySelectField(query_factory=ingredient_query, get_label="id", allow_blank=True)



    class Meta:
        csrf = False

class UpdateIngredientForm(FlaskForm):
    #id = IntegerField("Ingredient number", [validators.NumberRange(min=1, message="Please select an ingredient number from the list below.")])
    id = QuerySelectField(query_factory=ingredient_query, get_label="id", allow_blank=True)
    name = StringField("New ingredient name", [validators.Optional()])

    class Meta:
        csrf = False





