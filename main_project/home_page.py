from . import app
from flask_login import login_required, current_user

@app.route("/")
def home():
    if current_user.is_authenticated:
        return "Home page from logged in user."
    else:
        return "Home Page."

@app.route("/about")
@login_required
def about():
    return "About Page."

@app.route("/test")
def test():
    return "Test Page."