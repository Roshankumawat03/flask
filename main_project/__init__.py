from flask import Flask, render_template, request, url_for
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_profile.db"
app.secret_key = "sadflkadsjfbviwdslhv45hbjdsrqo8we7bcn89732"
login_manager = LoginManager(app)

from . import user_module
from . import login_logout
from . import home_page