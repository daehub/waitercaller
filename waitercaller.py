#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'

import config
import datetime
from bitlyhelper import BitlyHelper
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import LoginManager
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from user import User
from mockdbhelper import MockDBHelper as DBHelper
from passwordhelper import PasswordHelper
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
login_manager = LoginManager(app)
BH = BitlyHelper()
DB = DBHelper()
PH = PasswordHelper()
app.secret_key = 'ypzuLGRoE/pFeD/MyElW9N9HU/Qugm4ctGJHRDUb0vT4fRCtYDP4n6nOTAIGDgjQVgn6GhzM0D5R4ZOdmpCGgVV9E4hW0aCQml5'


@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)


@app.route('/')
def home(error_message=None):
    return render_template('home.html', error_message=error_message, registrationform=RegistrationForm(), loginform=LoginForm())


@app.route('/account')
@login_required
def account():
    tables = DB.get_tables(current_user.get_id())
    return render_template("account.html", tables=tables)


@app.route('/login', methods=['POST'])
def login():
    loginForm = LoginForm(request.form)
    if loginForm.validate():
        stored_user = DB.get_user(loginForm.loginemail.data)
        if stored_user and PH.validate_password(loginForm.loginpassword.data, stored_user['salt'].encode('utf-8'), stored_user['hashed']):
            user = User(loginForm.loginemail.data)
            login_user(user)
            return redirect(url_for('account'))
        # return account()
        loginForm.loginemail.errors.append("Email or password invalid")
    return render_template("home.html", loginform=loginForm, registrationform=RegistrationForm())


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/register', methods=['POST'])
def register():
    regForm = RegistrationForm(request.form)
    if regForm.validate():
        if DB.get_user(regForm.email.data):
            regForm.email.errors.append("Email address already registered")
            return render_template('home.html',registrationform=regForm)
        email = regForm.email.data
        salt = PH.get_salt()
        hashed = PH.get_hash(regForm.password.data+str(salt))
        DB.add_user(email,salt,hashed)
        return render_template("home.html", registrationform=regForm, onloadmessage="Registration successful. Please log in.", loginform=LoginForm())
    return render_template("home.html", registrationform=regForm, loginform=LoginForm())


@app.route("/account/createtable",methods=['POST'])
@login_required
def account_createtable():
    tableName = request.form.get("tablenumber")
    tableID = DB.add_table(tableName , current_user.get_id())
    new_URL = BH.shorten_url(config.base_url + "newrequest/" + tableID)
    DB.update_table(tableID, new_URL)
    return redirect(url_for('account'))


@app.route("/account/deletetable")
@login_required
def account_table():
    tableid = request.args.get('tableID')
    DB.delete_table(tableid)
    return redirect(url_for("account"))


@app.route('/newrequest/<tid>')
def new_request(tid):
    DB.add_request(tid,datetime.datetime.now())
    return "Your request has been looged and a waiter will be with you shortly"


@app.route("/dashboard")
@login_required
def dashboard():
    now = datetime.datetime.now()
    requests = DB.get_requests(current_user.get_id())
    for req in requests:
        deltaseconds = (now - req['time']).seconds
        req['wait_minutes'] = "{}.{}".format((deltaseconds/60),str(deltaseconds % 60).zfill(2))
    return render_template("dashboard.html", requests=requests)


@app.route('/dashboard/resolve')
@login_required
def dashboard_resolve():
    request_id = request.args.get("request_id")
    DB.delete_request(request_id)
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)