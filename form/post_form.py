from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired ,Length

class Post_form(FlaskForm):
    post_area= TextAreaField("text areafield",validators=[InputRequired("post cannot be empty!"),Length(max=200,message="your post is too big")])
