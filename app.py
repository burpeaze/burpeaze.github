from flask import Flask, render_template
import datetime
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year_copy = current_year)

@app.route('/get_started')
def get_started():
    return render_template('Get Started.html')


if __name__ == '__main__':
    app.run(debug=True)