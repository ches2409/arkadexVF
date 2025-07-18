from flask import Flask, render_template

from db import init_db
from models import roles, usuarios

import db

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

