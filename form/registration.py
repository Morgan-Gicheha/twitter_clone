from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired ,Length ,EqualTo

class Register_form(FlaskForm):
    name = StringField("Full names",validators=[InputRequired(), Length(max=100, message="name cannot be more than 100 charaters. ")])
    username = StringField("Username" , validators=[InputRequired("A username is required!"), Length(max=30, message="A username cannot be more that 30 charaters!")])
    password = PasswordField("Password should be secret!", validators=[ EqualTo ('confirm_password', message='Passwords must match')])
    confirm_password = PasswordField("Repeat password")
    image = FileField()