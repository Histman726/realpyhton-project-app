from flask_sqlalchemy import SQLAlchemy
from flask import Flask

import os


app = Flask(__name__)
app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

os.environ['LANG'] = 'en_GB.UTF-8'
os.environ['NIXPACKS_PYTHON_VERSION'] = '3.10'
os.environ['DATABASE_URL'] = 'postgresql+psycopg2://postgres:2486@localhost:5432/wordcount_dev'

from models import Result


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
