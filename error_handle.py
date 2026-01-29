from flask import Flask, request, abort

app = Flask(__name__)

# @app.route("/test")
# def take_form_data():
#     abort(401)
#     return "Test"

@app.errorhandler(404)
def a(error):
    return "This is a custom error message for 404 response.", 404

@app.route("/a")
def a():
    return "A"
