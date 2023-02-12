from flask import Flask
import os

app = Flask(__name__)
os.environ['LANG'] = 'en_GB.UTF-8'
os.environ['NIXPACKS_PYTHON_VERSION'] = '3.10'


@app.route('/')
def index():
    return 'Hola mundo'


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
