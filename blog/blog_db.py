from flask import Flask, request, render_template, redirect, url_for
from wtforms.ext.sqlalchemy.orm import model_form
import config
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def start():
    from models import Post
    article_form_class = model_form(Post, base_class=Form, db_session=db.session)

    form = article_form_class(request.form)

    if request.method == 'POST' and form.validate():
        article = Post(**form.data)
        db.session.add(article)
        db.session.commit()
    else:
        form = article_form_class()

    articles = Post.query.filter_by(is_visible=True)
    return render_template('index.html', form=form, articles=articles)


@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    article = Post.query.filter_by(id=id).first()
    article.is_visible = False
    db.session.commit()
    return redirect(url_for('hello'))


if __name__ == '__main__':
    from models import *

    db.create_all()
    app.run(host="0.0.0.0")
