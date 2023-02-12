from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola mundo'


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
