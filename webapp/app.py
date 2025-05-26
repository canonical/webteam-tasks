from canonicalwebteam.flask_base.app import FlaskBase
from flask import render_template

app = FlaskBase(
    __name__,
    "tasks-flask",
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/test")
def hello_world():
    return "<p>Hello, World!</p>"
