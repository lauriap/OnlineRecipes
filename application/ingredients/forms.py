from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, validators

class IngredientForm(FlaskForm):
    name = StringField("Ingredient name", [validators.Length(min=1)])

    class Meta:
        csrf = False


class DeleteIngredientForm(FlaskForm):
    id = IntegerField("Ingredient number", [validators.NumberRange(min=1, message="Please select an ingredient number from the list below.")])

    class Meta:
        csrf = False

class UpdateIngredientForm(FlaskForm):
    id = IntegerField("Ingredient number", [validators.NumberRange(min=1, message="Please select an ingredient number from the list below.")])
    name = StringField("New ingredient name", [validators.Optional()])

    class Meta:
        csrf = False



