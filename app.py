from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired ,Length 


app =Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:morgan8514@127.0.0.1:5432/twitter_clone "
app.config["SECRET_KEY"]= "secret"
app.config["DEBUG"]=True

db=SQLAlchemy(app)
migrate = Migrate(app, db)

# manager =Manager(app)
# manager.add_command('db' , MigrateCommand)

# importig the models/tables
from models.user import Register_user

# importing wtf forms
from form.registration import Register_form



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register" , methods=["POST","GET"])
def register():
    form= Register_form()
    # VALIDATING THE INPUTED VALUES BEFORE SUBMISSION
    if form.validate_on_submit():

        return "<h1> name: {} username: {} password {}".format(form.name.data, form.username.data, form.password.data)

    return render_template("register.html", form=form)


@app.route("/login")
def login():
    return ''

@app.route("/timeline")
def timeline():
    return render_template("timeline.html")

@app.route("/profile")
def profile():

    return render_template("profile.html")

@app.route("/logout")
def logout():

    return ""



if __name__=="__main__":
    manager.run()

