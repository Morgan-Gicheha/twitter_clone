from app import db

class Register_user(db.Model):
    """this is the registering a new user"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    username = db.Column(db.String(30))
    password = db.Column(db.String())
    profile_image= db.Column(db.String())



    # function to commit tothe db
    def create(self):
        db.session.add(self)
        db.session.commit()