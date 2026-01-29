from flask import Flask, render_template

app = Flask(__name__)


@app.route("/a")
def a():
    return render_template("a.html", title="A")

@app.route("/b")
def b():
    return render_template("b.html", title="B")

@app.route("/c")
def c():
    return render_template("c.html", title="C")

@app.route("/d")
def d():
    return render_template("d.html", title="D")

@app.route("/e")
def e():
    return render_template("e.html", title="E")