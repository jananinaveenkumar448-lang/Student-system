import csv
import os
import requests

from flask import Flask, render_template, request, redirect, flash
from models.db import (
    init_db,
    add_student,
    get_all_students,
    delete_student_by_id
)

app = Flask(__name__)
app.secret_key = "secret123"

init_db()

# ---------------- HELPERS ----------------

def get_quote():
    try:
        res = requests.get("https://api.quotable.io/random", timeout=5)
        if res.status_code == 200:
            return res.json()["content"]
    except:
        pass
    return "Keep learning and never give up!"


def save_to_csv(name, age, score):
    file_exists = os.path.isfile("students.csv")

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Name", "Age", "Score"])

        writer.writerow([name, age, score])

# ---------------- ROUTES ----------------

@app.route("/")
def home():
    students = get_all_students()
    return render_template("add_student.html", students=students)


@app.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    age = request.form.get("age")
    score = request.form.get("score")

    if not name or not age or not score:
        flash("All fields are required", "danger")
        return redirect("/")

    try:
        age = int(age)
        score = float(score)
    except:
        flash("Age and Score must be numbers", "danger")
        return redirect("/")

    add_student(name, age, score)
    save_to_csv(name, age, score)

    flash("Student added successfully!", "success")
    return redirect("/")


@app.route("/delete/<int:id>")
def delete(id):
    delete_student_by_id(id)
    flash("Student deleted!", "warning")
    return redirect("/")


@app.route("/leaderboard")
def leaderboard():
    students = get_all_students()
    quote = get_quote()
    return render_template("leaderboard.html", students=students, quote=quote)


# ---------------- ERROR HANDLERS ----------------

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)