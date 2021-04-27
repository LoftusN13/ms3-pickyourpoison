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
    return render_template("index.html")


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
        # bring user to their profile after successful login
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Log In page; registered users log in
    by entering their username and password.
    """
    if request.method == "POST":
        # see if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # checks if password matches for that user
        if existing_user:
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    # alert user to successful login
                    flash("Welcome, {}!".format(
                        request.form.get("username")))
                    # bring user to their profile after successful login
                    return redirect(url_for(
                        "profile", username=session["user"]))
            # password does not match for that user
            else:
                # alert user to unsuccessful login
                flash("Uh oh! Incorrect Username and/or Password!")
                return redirect(url_for("login"))

        # username does not exist in db
        else:
            flash("Uh oh! Incorrect Username and/or Password!")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
    Profile page; current session user's username
    pulled from db. Brought to their profile following
    successful login.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # if current session user; user is brought to their profile
    if session["user"]:
        return render_template("profile.html", username=username)

    # else redirects user to Log In
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Logout; current user is removed from
    session. session cookies removed
    """
    # alert user to successful logout
    flash("You have logged out. See you later!")
    session.pop("user")
    # redirect user to Log In page
    return redirect(url_for("login"))


@app.route("/get_cocktails")
def get_cocktails():
    # pulls recipe data from db
    recipes = mongo.db.recipes.find()
    return render_template("cocktails.html", recipes=recipes)


@app.route("/new_cocktail", methods=["GET", "POST"])
def new_cocktail():
    """
    New Recipe Page; registered user can create
    a new cocktail recipe. When the user submits
    the new recipe form, the recipe will be
    added to the db
    """
    if request.method == "POST":
        cocktail = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_ingredients": request.form.get("cocktail_ingredients"),
            "cocktail_steps": request.form.get("cocktail_steps"),
            "cocktail_image": request.form.get("cocktail_image"),
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(cocktail)
        # Alert user to successful recipe added
        flash("Amazing! Another delicious cocktail added!")
    # Alcohol categories pulled from db for select menu
    categories = mongo.db.categories.find()
    return render_template("new_cocktail.html", categories=categories)


@app.route("/edit_cocktail/<recipe_id>", methods=["GET", "POST"])
def edit_cocktail(recipe_id):
    """
    Edit Cocktail; creator of the recipe can
    edit it. On submit, db will be searched
    for the current recipe by its id. When
    found, recipe in db will be updated
    using the new entries in the edit recipe
    form.
    """
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "cocktail_name": request.form.get("cocktail_name"),
            "cocktail_ingredients": request.form.get("cocktail_ingredients"),
            "cocktail_steps": request.form.get("cocktail_steps"),
            "cocktail_image": request.form.get("cocktail_image"),
            "created_by": session["user"]
        }
        # correct recipe will be updated using submit dictionary
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        # Alert user to successful recipe edit
        flash("All done! Your delicious recipe has been edited!")

    # searches db for the correct cocktail recipe by id
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    return render_template(
        "edit_cocktail.html", recipe=recipe, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
