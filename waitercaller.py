#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'


from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from user import User
from mockdbhelper import MockDBHelper as DBHelper
from passwordhelper import PasswordHelper

app = Flask(__name__)
login_manager = LoginManager(app)
DB = DBHelper()
PH = PasswordHelper()
app.secret_key = 'ypzuLGRoE/pFeD/MyElW9N9HU/Qugm4ctGJHRDUb0vT4fRCtYDP4n6nOTAIGDgjQVgn6GhzM0D5R4ZOdmpCGgVV9E4hW0aCQml5'


@app.route('/')
def home(error_message=None):
    return render_template('home.html',error_message = error_message)


@app.route('/account')
@login_required
def account():
    return "You are logged in !"


@app.route('/login', methods=['POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    stored_user = DB.get_user(email)
    if stored_user and PH.validate_password(password,stored_user['salt'].encode('utf-8'),stored_user['hashed']):
        user = User(email)
        login_user(user)
        return redirect(url_for('account'))
        # return account()
    return home()


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    pw1 = request.form.get('password')
    pw2 = request.form.get('password2')
    if not pw1 == pw2 :
        return redirect(url_for('home'))
    if DB.get_user(email):
        return redirect(url_for('home'))
    salt = PH.get_salt()
    hashed = PH.get_hash(pw1+str(salt))
    DB.add_user(email,salt,hashed)
    return redirect(url_for('home'))


@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)


if __name__ == '__main__':
    app.run(port=5000, debug=True)