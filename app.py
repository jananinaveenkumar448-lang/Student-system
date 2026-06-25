from flask import Flask, render_template, request, redirect, session, flash
from models.db import *

app = Flask(__name__)
app.secret_key = "secret123"

init_db()
@app.route("/")
def home():
    if "user_id" in session:
        return redirect("/dashboard")
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        success = add_user(request.form["username"], request.form["password"])

        if success:
            flash("Account created!", "success")
            return redirect("/login")
        else:
            flash("Username already exists!", "danger")
            return redirect("/register")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        user = get_user(request.form["username"])

        if user and user[2] == request.form["password"]:
            session["user_id"] = user[0]
            session["username"] = user[1]
            return redirect("/dashboard")

        flash("Invalid login", "danger")

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect("/login")

    students = get_students(session["user_id"])

    return render_template("dashboard.html", students=students)

@app.route("/add", methods=["POST"])
def add():

    if "user_id" not in session:
        return redirect("/login")

    add_student(
        request.form["name"],
        int(request.form["age"]),
        float(request.form["test1"]),
        float(request.form["test2"]),
        float(request.form["test3"]),
        session["user_id"]
    )

    return redirect("/dashboard")

@app.route("/delete/<int:id>")
def delete(id):

    delete_student(id)
    return redirect("/dashboard")

@app.route("/leaderboard")
def leaderboard():

    if "user_id" not in session:
        return redirect("/login")

    students = get_students(session["user_id"])

    return render_template("leaderboard.html", students=students)



@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)