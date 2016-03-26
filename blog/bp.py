from flask import Blueprint, render_template, abort, request
from jinja2 import TemplateNotFound
from flask_login import LoginManager

auth = Blueprint('login', __name__, url_prefix='/auth')


@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        pass #hz chto


@auth.route('/logout', methods=['GET','POST'])
def logout():
    pass








