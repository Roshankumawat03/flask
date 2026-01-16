from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return f"""<h1>Hello, World!</h1>
    <a href="{url_for("about")}">About</a>
    <a href="{url_for("learn_url_for")}">learn Url</a>
    """


@app.route("/about")
def about():
    return "<h2>This is about page</h2>"

@app.route("/greet/<name>")
def greet(name):
    return f"""
<h1>Hi {name}</h1>
This is test website.
"""

@app.route("/age/<int:age>")
def vote_validation(age):
    if age > 18:
        return """
<h4 style="color:green">Yes You Can Vote</h4>
"""
    else:
        return """
<h4 style="color:red">No You Can Not Vote</h4>
"""


@app.route("/path/<path:abc>")
def learn_path(abc):
    return abc

@app.route("/test_urls")
def learn_url_for():
    return url_for("about")