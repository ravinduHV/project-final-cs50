from flask import Flask, redirect, request, render_template, session
from flask_session import Session
from cs50 import SQL

from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import login_required, apology


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
    return render_template("index.html")
    

@app.route("/login", methods=["POST","GET"])
def login():
    """Log user in"""
    # clearing previous sessions
    session.clear()

    if request.method == "POST":
        #Check for credentials
        username = request.form.get("username")
        password = request.form.get("password")
        #check for availabilty in database
        return redirect("/")

    else:
        return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        #record new user
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")
        tele_num =request.form.get("tele_num")
        address = request.form.get("address")
        if not username or not password or not confirmation or not email or not tele_num or not address:
            return apology("Must complete all the fields", 400)

        info_by_username = db.execute("SELECT * FROM users WHERE username = ?", username)
        if info_by_username:
            return apology("Username is already taken", 400)

        info_by_email = db.execute("SELECT * FROM users WHERE email = ?", email)
        if info_by_email:
            return apology("Email is already taken", 400)

        info_by_teleN = db.execute("SELECT * FROM users WHERE phone_number = ?", tele_num)
        if info_by_teleN:
            return apology("Mobile Number is already taken", 400)
        
        if password != confirmation:
            return apology("The password confirmation does not match", 400)

        db.execute("INSERT INTO users (username, email, phone_number, Address, hash) VALUES(?, ?, ?, ?, ?)", username, email, tele_num, address, generate_password_hash(password))

        row = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = row[0]["id"]
        
        return redirect("/")

    else:
        return render_template("register.html")