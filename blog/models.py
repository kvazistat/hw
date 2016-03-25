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
