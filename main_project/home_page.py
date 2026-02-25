from . import app, render_template, flash
from flask_login import login_required, current_user

@app.route("/")
def home():
    # if current_user.is_authenticated:
    #     return "Home page from logged in user."
    # else:
    # flash("Hi I am the flashed message.")

    #/ if current_user.is_authenticated:
    #     flash("You are logged in.")
    # else:
    #     flash("You are not logged in.") /   
    return render_template("home.html", title = "Home")

@app.route("/about")
@login_required
def about():
    return "About Page."

@app.route("/test")
def test():
    return render_template("test.html", current_user=current_user)