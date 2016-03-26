from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from blog_db import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(150), nullable=False)
    title = db.Column(db.String(140), nullable=False, unique=False)
    content = db.Column(db.String(3000), nullable=False)
    is_visible = db.Column(db.Boolean)

    def __init__(self, author, title, content, is_visible):
        self.title = title
        self.author = author
        self.content = content
        self.is_visible = True


class User(db.Model):
    id = db.Column('user_id', db.Integer, primary_key=True)
    login = db.Column('login', db.String(150), nullable=False, unique=True)
    password = db.Column('password', db.String(140), nullable=False)
    email = db.Column('email', db.String(100), nullable=False, unique=True)
    reg_time = db.Column('reg_time', db.DateTime)

    def __init__(self, login=None, email=None):
        self.login = login
        self.email = email
        self.reg_time = datetime.utcnow()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<kek %s>' % self.login
