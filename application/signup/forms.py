from flask_wtf import SignUpForm
from wtforms import StringField

class SignUpForm(FlaskForm):
    name = StringField("Name")
    nickname = StringField("Nickname")
    password = StringField("Password")
 
    class Meta:
        csrf = False
