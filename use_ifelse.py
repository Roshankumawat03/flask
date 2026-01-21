from flask import Flask, render_template, request
from data import user_data
user_data = user_data["users"]

app = Flask(__name__)


@app.route("/check_div/<int:number>")
def div_by_5_and_3(number):
    return render_template("check_div.html", number=number)


@app.route("/list")
def list_users():
    return render_template("list_users.html", title="List Users", user_list=user_data)


@app.route("/watch")
def get_request_data():
    v = request.args.get("v")
    return render_template("yt.html", title="Play Video", v=v)