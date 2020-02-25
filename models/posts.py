from main import db
from flask_login import UserMixin

class Posts(UserMixin ,db.Model):
    '''this class stores the posts'''
    id = db.Column(db.Integer, primary_key=True)
    user_id= db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False )
    date_posted = db.Column(db.DateTime, nullable=False)
    post= db.Column(db.String(),nullable=False)


    # method to commit to db
    
    def create(self):
        db.session.add(self)
        db.session.commit()