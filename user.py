from flask import Flask, render_template
from data import user_data
user_data = user_data["users"]

app = Flask(__name__)


# @app.route("/get_users")
# def get_all_users():
#     a = []
#     for x in user_data:
#         a.append(
#             f"""<h3>{x.get("firstName")}</h3>
#             <h4>{x.get("lastName")}</h4>
#             """
#         )
#     return "<br>".join(a)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/username/<username>")
def username(username):
    return render_template("about_user.html", name=username)