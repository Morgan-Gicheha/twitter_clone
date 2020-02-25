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
from datetime import datetime

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
app.config["UPLOADS_DEFAULT_URL"] = "'http://127.0.0.1:5000/_uploads/photos/download (1).jpg'"

configure_uploads(app,photos)

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.filter_by(id=user_id).first()    

db=SQLAlchemy(app)
# importing time
from other_dependancies.time_func import time_
from other_dependancies.time_func import time_post

# importig the models/tables
from models.user import Users
from models.posts import Posts
from models.junction import followers

# importing wtf forms
from form.registration import Register_form
from form.login import Login_form
from form.post_form import Post_form
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
            image_filename = form.image.data
            # saving the image passed to specified folder
            # image_filename=photos.save(form.image.data)
            if not  image_filename:
                image_filename=  'C:/Users/giche/Desktop/protect/twitter_clone/download (1).jpg'
                
            image_filename_=photos.save(image_filename)
            # getting_image url
            image_url = photos.url(image_filename_)
            
            # getting date  whent account was created/caliing function
            now_today= time_()
            
            # sending data to dd

            info = Users(name=name, username=username, password=generate_password_hash(password),joined_on=now_today ,profile_image=image_url)
            info.create()
            
            return render_template("index.html", form=form, message="Account created! Now Login..")

    return render_template("register.html", form=form)


@app.route("/login", methods=["POST","GET"])
def login():
    form = Login_form()
    if form.validate_on_submit():
        if request.method=="POST":
            username= form.username.data
            password = form.password.data
            remember_me = form.remember_me.data

            check_if_user_exist= Users.query.filter_by(username=username).first()
            if not check_if_user_exist:
                message= "no such username found!"
                print(message)
                return render_template("index.html" , form=form, message_user=message)


            checkin_username_and_password=Users.pass_username_check(username=username, password=password)
            if checkin_username_and_password:
                login_user(check_if_user_exist,remember=form.remember_me.data)
                print("loged in")
                return redirect(url_for("profile"))
               
                # logging in the user. flask login does th session for us . not that this is after all credential verification has been verified

            else:
                message= "wrong password!"
                print(message)
                return render_template("index.html" , form=form, message_password=message)
                
            
            
            

    return redirect(url_for("home"))

# creating a post tweet route
@app.route("/post", methods=["POST","GET"])
@login_required
def post_tweet():
    form= Post_form()
    if form.validate_on_submit():
        if request.method=="POST":
            content= form.post_area.data
            # sending info to db
            time_post_var=time_post()
            post=Posts(user_id=current_user.id, post=content, date_posted=time_post_var)
            post.create()
            print("post posted")
            return redirect(url_for('timeline'))



@app.route("/timeline" ,defaults={'username':None})
@app.route("/timeline/<username>", methods=["POST","GET"])
@login_required
def timeline(username):
    form= Post_form()
    
    # quering for username this query will only run if the the username is passed in: else it will jump to the default user in session
    if username:
        user= Users.query.filter_by(username= username).first()
        if not user:
            return 'user not found'
        
        current_user_id =  user.id
        user_=user
    else:
        current_user_id= current_user.id
        user = current_user
        user_= current_user


        # getting all posts for all followee.... followee is the person being followed..the below query joins posts by the followee to theuser id in the posts table
        # thus it will get all posts of being followed by the logged in user
    all_posts_timeline = Posts.query.join(followers,(followers.c.followee_id_followee==Posts.user_id)).filter(followers.c.me_user_id_follower==user.id).order_by(Posts.date_posted.desc()).all()
    # getting all posts
    # all_posts_timeline = Posts.query.filter_by(user_id=current_user_id).order_by(Posts.date_posted.desc()).all()
    # geting current time
    # print(all_posts_timeline)
    current_time =datetime.now()
    
    # getting total number of tweets
    total_tweets= Posts.query.filter_by(user_id=current_user_id).all()
    # print(len(total_tweets))

    # followed by
    followed_by = user_.followed_by.all()
    
    # getting random users from the database for the who to whatch section
    who_to_watch = Users.query.filter(Users.id != current_user_id ).order_by(db.func.random()).limit(4).all()
    return render_template("timeline.html", form=form, all_posts = all_posts_timeline, current_time=current_time, total_tweets=total_tweets, user=user, who_to_watch=who_to_watch, followed_by=followed_by)
  
# time since post created
# incomplete
@app.template_filter("div_mode")
def div_mode(delta):
    seconds = delta.total_seconds()
    # rounding  of seconds to a whole digit
    seconds = round(seconds)
    # print(seconds)
    day ,seconds= divmod(seconds,86400 )
    hour, seconds = divmod(seconds,3600)
    minute, seconds= divmod(seconds, 60)

    if day >0:
        return f'{day}d'
    elif hour > 0:
        return f'{hour}h'
    elif minute > 0:
        return f'{minute}m'
    else:
        return f'{seconds}s'



@app.route("/profile", defaults={'username':None})
@app.route("/profile/<username>", methods=["POST","GET"])
@login_required
def profile(username):
    if username:
        # if username.. query database for username and return object
        user = Users.query.filter_by(username=username).first()
        if not user:
            return "user not found"
        current_user_= user
    # and if not username run the below code
    else:

        current_user_=current_user
    # quering for all posts
    all_posts = Posts.query.filter_by(user_id=current_user_.id).order_by(Posts.date_posted.desc()).all()
    # print(all_posts)
    current_time =datetime.now()
    # getting list of follwers
    followed_by = current_user_.followed_by.all()
    # print(len(followers_by))
    # for any in followed_by:
    #     print(any.password)

    display_follow=True
    # checking is the user is the user in session
    if current_user == current_user_:
        display_follow= False
    elif current_user in followed_by :
        # checking if the user to follow is allready followed
            display_follow= False

    # getting random users from the database for the who to whatch section
    who_to_watch = Users.query.filter(Users.id != current_user_.id ).order_by(db.func.random()).limit(4).all()
    # for x in who_to_watch:
    #     print(x.username)

  


    return render_template("profile.html",current_user=current_user_, all_posts=all_posts, current_time=current_time, followed_by=followed_by, display_follow=display_follow, who_to_watch=who_to_watch)

# follow route
@app.route("/follow/<username>")
@login_required
def follow(username):
    user_to_follow = Users.query.filter_by(username=username).first()

    current_user.following.append(user_to_follow)
    db.session.commit()
    return redirect(url_for("profile"))



# logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))



if __name__=="__main__":
    manager.run()

