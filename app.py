from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = "fitplanhub_secret"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from auth import *
from trainer import *
from user import *

if __name__ == "__main__":
    app.run(debug=True)
