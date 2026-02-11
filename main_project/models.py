from . import app, login_manager

from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy(app)


class User(database.Model):

    id = database.Column(database.Integer, primary_key = True)
    username = database.Column(database.String(10), unique=True, nullable=False)
    email = database.Column(database.String(100), unique=True, nullable=False)
    password = database.Column(database.String(30), nullable=False)
    name = database.Column(database.String(200))
    profile_photo = database.Column(database.String(200), default= "static/profilephoto/default.png")


    def __repr__(self):
        return f"<{self.id}, {self.name}, {self.username}>"


with app.app_context():
    database.create_all()


@login_manager.user_loader
def get_user(user_id):
    return User.query.get(int(user_id))