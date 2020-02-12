from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy 
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand 
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired ,Length 
from  flask_wtf.file import FileField, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,UserMixin,logout_user,login_fresh,login_required,logout_user, login_user, current_user

app =Flask(__name__)



@app.before_first_request
def create():
    db.create_all()
# configuring database
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres:morgan8514@127.0.0.1:5432/twitter_clone"
app.config["SECRET_KEY"]= "secret"
app.config["DEBUG"]=True
# configuring uploads
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "pictures"
configure_uploads(app,photos)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Register.query.filter_by(id=user_id).first()    

db=SQLAlchemy(app)
# importing time
from other_dependancies.time_func import time_

# importig the models/tables
from models.user import Register

# importing wtf forms
from form.registration import Register_form
from form.login import Login_form
# routes
@app.route("/",methods=["POST","GET"])
def home():
    form = Login_form()


    return render_template("index.html" , form=form)



@app.route("/register" , methods=["POST","GET"])
def register():
    form= Register_form()
    # VALIDATING THE INPUTED VALUES BEFORE SUBMISSION
    if form.validate_on_submit():
        if request.method =="POST":
            # recieving data from register form
            name = form.name.data
            username = form.username.data
            password = form.password.data

            # saving the image passed to specified folder
            image_filename=photos.save(form.image.data)
            # getting_image url
            image_url = photos.url(image_filename)
            
            # getting date  whent account was created
            now_today= time_()
            
            # sending data to dd

            info = Register(name=name, username=username, password=generate_password_hash(password),joined_on=now_today ,profile_image=image_url)
            info.create()
            
            return render_template("index.html", form=form, message="Account created! Now Login..")

    return render_template("register.html", form=form)


@app.route("/login", methods=["POST"])
def login():
    form = Login_form()
    if form.validate_on_submit():
        if request.method=="POST":
            username= form.username.data
            password = form.password.data
            remember_me = form.remember_me.data

            check_if_user_exist= Register.query.filter_by(username=username).first()
            if not check_if_user_exist:
                message= "no such username found!"
                print(message)
                return render_template("index.html" , form=form, message_user=message)


            checkin_username_and_password=Register.pass_username_check(username=username, password=password)
            if checkin_username_and_password:
                login_user(check_if_user_exist)
                print("loged in")
                return redirect(url_for("profile"))
               
                # logging in the user. flask login does th session for us . not that this is after all credential verification has been verified

            else:
                message= "wrong password!"
                print(message)
                return render_template("index.html" , form=form, message_password=message)
                
            
            
            

    return redirect(url_for("home"))

@app.route("/timeline")
def timeline():



    return render_template("timeline.html")

@app.route("/profile")
@login_required
def profile():
    # current user returns the object of the user that is logged in
    
    return render_template("profile.html",current_user=current_user)

# logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))



if __name__=="__main__":
    manager.run()

