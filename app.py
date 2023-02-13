from flask import Flask
import os

app = Flask(__name__)
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

os.environ['LANG'] = 'en_GB.UTF-8'
os.environ['NIXPACKS_PYTHON_VERSION'] = '3.10'
os.environ['SECRET_KEY'] = 'key-read-from-env-var'


@app.route('/')
def index():
    secret_key = app.config.get("SECRET_KEY")
    return f"The configured secret key is {secret_key}."


if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
