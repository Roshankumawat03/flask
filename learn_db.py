from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///roshan.db"

db = SQLAlchemy(app)

class Mytable(db.Model):
    pr_key = db.Column(db.Integer, primary_key=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

u1 = User(is_admin=False, username="rohan", email="rohan@gmail.com", password="12345")
u2 = User(is_admin=False, username="aman", email="aman@gmail.com", password="12345")
u3 = User(is_admin=False, username="naman", email="naman@gmail.com", password="12345")
u4 = User(is_admin=True, username="aryan", email="aryan@gmail.com", password="12345")
u5 = User(is_admin=True, username="sahil", email="sahil@gmail.com", password="12345")
u6 = User(is_admin=True, username="sohan", email="sohan@gmail.com", password="12345")
   

# with app.app_context():
#     db.create_all()
#     db.session.add(u1)
#     db.session.add(u2)
#     db.session.add(u3)
#     db.session.add(u4)
#     db.session.add(u5)
#     db.session.add(u6)
#     db.session.commit()


# with app.app_context():
#     user = User.query.get(1)
#     user.username = "rahul"
#     user.email = "rk@gmail.com"
#     db.session.commit()


# with app.app_context():
#     user = User.query.get(2)
#     db.session.delete(user)
#     db.session.commit() 

with app.app_context():
    user = User.query.get(3)
    db.session.commit()
    print(user.username)



# with app.app_context():
#     db.create_all()
#     for x in range(100):
#         a = Mytable()
#         db.session.add(a)
#     db.session.commit()