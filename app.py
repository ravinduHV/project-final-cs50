from flask import Flask, flask, redirect, request, render_templates, session
from flask_session import Session
from cs50 import SQL

from helpers import login_required


# config app
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///traveller.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
@login_required
def index():
    # font page(main)
    # display new feed


@app.route("/login" methods=["POST","GET"])
def login():
    # clearing previous sessions
    session.clear()

    if request.method == "POST":

        #Check for credentials
        return None 

    else:
        return render_template("login.html")