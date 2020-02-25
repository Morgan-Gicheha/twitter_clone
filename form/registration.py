from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired ,Length ,EqualTo

class Register_form(FlaskForm):
    name = StringField("Full names",validators=[InputRequired(), Length(max=200, message="name cannot be more than 100 charaters. ")])
    username = StringField("Username" , validators=[InputRequired("A username is required!"), Length(max=30, message="A username cannot be more that 30 charaters!"), Length(min=4, message="username too short")])
    password = PasswordField("Password should be secret!", validators=[ EqualTo ('confirm_password', message='Passwords must match'), Length(min=5, message="password too short")])
    confirm_password = PasswordField("Repeat password")
    image = FileField()
    # image = FileField("profile img is required", validators=[InputRequired("A pic is required!")])