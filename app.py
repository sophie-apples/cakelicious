import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/getrecipes")
def getrecipes():
    recipes = mongo.db.recipes.find()
    return render_template("getrecipes.html", recipes=recipes)
    

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into session cookie
        session["user"] = request.form.get("username").lower()
        flash("registration sucessful")
        return redirect(url_for("myrecipes", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check is username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check password
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "myrecipes", username=session["user"]))
            else:
                # invalid password
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            # invalid username
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/myrecipes/<username>", methods=["GET", "POST"])
def myrecipes(username):

    # get session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # display recipes by session user from db ()
    if session["user"]:
        # display recipes added by the user
        myrecipes = mongo.db.recipes.find({
            "user": session["user"]})
        return render_template(
            "myrecipes.html", username=username, recipes=myrecipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("you've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/addrecipe", methods=["GET", "POST"])
def addrecipe():
    if request.method == "POST":
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "equipment": request.form.get("equipment").splitlines(),
            "ingredients": request.form.get("ingredients").splitlines(),
            "method": request.form.get("method").splitlines(),
            "user": session["user"],
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe successfully added! Yum!")
        return redirect(url_for("getrecipes"))

    return render_template("addrecipe.html")


@app.route("/editrecipe/<recipe_id>", methods=["GET", "POST"])
def editrecipe(recipe_id):
    if request.method == "POST":
        submit = {
            "recipe_name": request.form.get("recipe_name"),
            "recipe_description": request.form.get("recipe_description"),
            "equipment": request.form.get("equipment").splitlines(),
            "ingredients": request.form.get("ingredients").splitlines(),
            "method": request.form.get("method").splitlines(),
            "user": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe successfully updated!")

    recipe = mongo.db.recipes.find_one(
        {"_id": ObjectId(recipe_id)})
    return render_template("editrecipe.html", recipe=recipe)


@app.route("/deleterecipe/<recipe_id>")
def deleterecipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe successfully deleted.")
    return redirect(url_for("getrecipes"))


@app.errorhandler(404)
def page_not_found(error):
    # 404
    return render_template('404.html', page_title='404'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
