from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_profile.db"

database = SQLAlchemy(app)

class User(database.Model):

    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String(10), unique=True, nullable=False)
    email = database.Column(database.String(100), unique=True, nullable=False)
    password = database.Column(database.String(30), unique=True, nullable=False)
    name = database.Column(database.String(200))
    profile_photo = database.Column(database.String(200), default= "static\profilephoto\default.png")

with app.app_context():
    database.create_all()

@app.route("/register")
def register():
    return render_template("user_register.html", title="Register Page")


@app.route("/validate_data", methods=["POST"])
def validate_data():
    name = request.form.get("name")
    email = request.form.get("mail")
    username = request.form.get("username")
    password = request.form.get("password")
    image = request.files.get("photo")

    if all((username, password, email)):

        data_to_dump = User(
            name = name,
            email = email,
            username = username,
            password = password
        )
        if image:
            photo_path = "profilephoto/" + username + ".png"
            image.save("static/" + photo_path)
            data_to_dump.profile_photo = photo_path

        database.session.add(data_to_dump)
        database.session.commit()
        return "User Created Done."
    else:
        return "You did not pass all the required values.", 409


@app.route("/get_user_by_id/<int:id>")
def get_user_by_id(id):
    
    user_info = User.query.get(id)
    return render_template(
        "profile.html",
        name=user_info.name,
        username=user_info.username,
        email=user_info.email,
        profile_photo=user_info.profile_photo[7:]
    )


