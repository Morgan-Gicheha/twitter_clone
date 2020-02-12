from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, BooleanField
from wtforms.validators import InputRequired ,Length 

class Login_form(FlaskForm):
    username = StringField("username" , validators=[InputRequired("A usernam is required!"),Length(max=100, message="Username cannot be more than 100 characters")])
    password = PasswordField("password", validators=[InputRequired("password is required!"), Length(max=30, message="password cannot be more than 30 charactors")])
    remember_me = BooleanField("remember")