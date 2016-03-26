from flask_wtf import Form
from wtforms_alchemy import model_form_factory

kek = model_form_factory(Form)

def password_match(form, field):
    if form.password.data != field.data:
        raise ValueError('Error!!1')

def LoginForm(form):
    #def __init__(self, )
    pass
