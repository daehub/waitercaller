#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Daehub'


from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home(error_message = None):
    return render_template('home.html',error_message = error_message)


if __name__ == '__main__':
    app.run(port=5000, debug=True)