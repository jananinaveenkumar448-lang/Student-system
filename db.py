import sqlite3

DB = "students.db"

def get_connection():
    return sqlite3.connect(DB)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            score REAL,
            user_id INTEGER
        )
    """)

    conn.commit()
    conn.close()


# ---------------- USERS ----------------

def add_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, password)
    )

    conn.commit()
    conn.close()


def get_user(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=?",
        (username,)
    )

    user = cur.fetchone()
    conn.close()
    return user


# ---------------- STUDENTS ----------------

def add_student(name, age, score, user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (name, age, score, user_id)
        VALUES (?, ?, ?, ?)
    """, (name, age, score, user_id))

    conn.commit()
    conn.close()


def get_all_students(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM students WHERE user_id=?
    """, (user_id,))

    data = cur.fetchall()
    conn.close()
    return data


def delete_student_by_id(student_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()