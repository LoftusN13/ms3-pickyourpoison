import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    recipes = mongo.db.recipes.find()
    return render_template("base.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Registration page; users can create an account
    by entering a username and password.
    """
    if request.method == "POST":
        # see if username is already taken/exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # alert user if username is already taken/exists
        if existing_user:
            flash("Sorry, this username is already taken! Try another one!")
            return redirect(url_for("register"))

        # takes the user's form info and inserts it into mongo users db
        new_user = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(new_user)

        # alert user that registration is successful
        session["user"] = request.form.get("username").lower()
        flash("Registration Complete! Welcome!")

    return render_template("register.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
