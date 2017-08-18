import os
from flask import Flask, render_template
from data import data

f = open('index.html', 'w+')
app = Flask(__name__)


with app.app_context():
    print(type(render_template('index.html', data=data)))
    f.write(render_template('index.html', data=data))

f.closed
