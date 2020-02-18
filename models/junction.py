# followers function
from app import db

followers = db.Table("follower_followee_jk", 
                    db.Column("me_user_id_follower",db.Integer,db.ForeignKey("users.id")),
                    db.Column("followee_id_followee", db.Integer, db.ForeignKey("users.id")))