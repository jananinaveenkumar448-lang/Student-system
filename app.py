from flask import Flask, render_template, request, redirect, flash
import sqlite3
import requests
from models.db import init_db

app = Flask(__name__)
app.secret_key = "secret123"

init_db()


# ---------------- API ----------------
def get_quote():
    try:
        res = requests.get("https://api.quotable.io/random", timeout=5)
        if res.status_code == 200:
            return res.json()["content"]
    except:
        pass
    return "Keep learning and never give up!"


# ---------------- HOME ----------------
@app.route("/")
def home():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()

    return render_template("add_student.html", students=students)


# ---------------- ADD ----------------
@app.route("/add", methods=["POST"])
def add_student():

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

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students (name, age, score)
        VALUES (?, ?, ?)
    """, (name, age, score))

    conn.commit()
    conn.close()

    flash("Student added successfully!", "success")
    return redirect("/")


# ---------------- DELETE ----------------
@app.route("/delete/<int:id>")
def delete_student(id):

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    flash("Student deleted!", "warning")
    return redirect("/")


# ---------------- LEADERBOARD ----------------
@app.route("/leaderboard")
def leaderboard():

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM students
        ORDER BY score DESC
    """)

    students = cursor.fetchall()
    conn.close()

    quote = get_quote()

    return render_template(
        "leaderboard.html",
        students=students,
        quote=quote
    )


# ---------------- ERROR PAGES ----------------
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500


# ---------------- RUN ----------------
if __name__ == "__main__":
    app.run(debug=True)