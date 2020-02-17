# followers function
from app import db

followers = db.Table("follower_followee_jk", 
                    db.Column("me_user_id",db.Integer,db.ForeignKey("users.id")),
                    db.Column("follower_id", db.Integer, db.ForeignKey("users.id")))