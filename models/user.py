from app import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class Users(UserMixin ,db.Model):
    """this is the registering a new user"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(30))
    password = db.Column(db.String(100))
    joined_on = db.Column(db.Date)
    profile_image= db.Column(db.String(100))
    user=db.relationship("Posts", backref='this_user')



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
        
            
