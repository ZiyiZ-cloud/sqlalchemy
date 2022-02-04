"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

default_time = datetime.now()

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"
    
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
    
class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False,
                     )
    last_name = db.Column(db.String(50),
                     nullable=False,
                     )
    image_url = db.Column(db.Text,
                          nullable= False,
                          default = DEFAULT_IMAGE_URL)
    
class Post(db.Model):
    
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.String(50),
                     nullable=False,
                     )
    content = db.Column(db.Text,
                     nullable=False,
                     )
    created_at = db.Column(db.Text,
                          nullable= False,
                          default = default_time)
    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'),
                          nullable= False)
    
    userid = db.relationship('User', backref = 'post')
