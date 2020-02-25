from main import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from models.junction import followers

class Users(UserMixin ,db.Model):
    """this is the registering a new user"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(30))
    password = db.Column(db.String())
    joined_on = db.Column(db.Date)
    profile_image= db.Column(db.String())
    user=db.relationship("Posts", backref='this_user')
    
    # this is a query and it returns allm people that the curent user is following::: soo basically the cureent user is on the left of the table while\
    # his/her follwers are on the right handside of the table
    following = db.relationship("Users", secondary="follower_followee_jk",
                                primaryjoin=(followers.c.me_user_id_follower==id),
                                secondaryjoin=(followers.c.followee_id_followee==id),
                                backref=db.backref("followers", lazy="dynamic"), lazy="dynamic")


    # # this query returns all peape that follw the current user
    followed_by = db.relationship("Users", secondary=followers, 
                                primaryjoin=(followers.c.followee_id_followee==id), 
                                secondaryjoin=(followers.c.me_user_id_follower==id), backref=db.backref("poeple_following_me", lazy="dynamic"), lazy="dynamic" )
    # function to commit tothe db
    def create(self):
        db.session.add(self)
        db.session.commit()

    # checking password and username
    @classmethod
    def pass_username_check (cls,username, password):
        username_check = cls.query.filter_by(username=username).first()
        if username_check and check_password_hash(username_check.password, password):
            return True
        else:
            return False
        
            
