#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'

from wtforms import Form
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms import StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class RegistrationForm(Form):
    email = EmailField('email', [validators.required(), validators.Email()])
    password = PasswordField('password',  [validators.required(), validators.Length(min=8,message="Please choose a password of at least 8 characters")])
    password2 = PasswordField('password2', [validators.required(), validators.EqualTo('password',message='Passwords must match')])
    submit = SubmitField('submit', [validators.DataRequired()])


class LoginForm(Form):
    loginemail = EmailField('email',[validators.DataRequired(),validators.Email()])
    loginpassword = PasswordField('password',[validators.data_required(message="Password field is required")])
    submit = SubmitField('submit',[validators.DataRequired()])


class TableForm(Form):
    tableID = StringField('tablename',[validators.DataRequired()])
    submit = SubmitField('submit',[validators.DataRequired()])

if __name__ == '__main__':
    app = False(__name__)
    app.run(port=5000, debug=True)

