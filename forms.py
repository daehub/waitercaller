#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'

from flask_wtf import Form
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from flask import Flask
from flask import render_template


class RegistrationForm(Form):
    email = EmailField('email', [validators.required(), validators.Email()])
    password = PasswordField('password',  [validators.required(), validators.Length(min=8,message="Please choose a password of at least 8 characters")])
    password2 = PasswordField('password2', [validators.required(), validators.EqualTo('password',message='Passwords must match')])
    submit = SubmitField('submit', [validators.DataRequired()])


app = Flask(__name__)
app.secret_key = 'ypzuLGRoE/pFeD/MyElW9N9HU/Qugm4ctGJHRDUb0vT4fRCtYDP4n6nOTAIGDgjQVgn6GhzM0D5R4ZOdmpCGgVV9E4hW0aCQml5'


@app.route("/")
def home():
    RGForm = RegistrationForm()
    return render_template('index.html', registerForm=RGForm)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

