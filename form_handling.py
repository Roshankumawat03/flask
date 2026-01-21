from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/signup")
def take_form_data():
    return render_template("register.html", title="Register")


@app.route("/data_validation", methods=["POST"])
def validation_data():
    username = request.form.get("username")
    mail = request.form.get("mail")
    password = request.form.get("password")

    if all([username, mail, password]):
        return render_template("data_valid.html", login = True)
    else:
        return render_template("data_valid.html", login = False)
    