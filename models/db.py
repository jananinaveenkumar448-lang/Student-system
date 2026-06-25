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
        test1 REAL,
        test2 REAL,
        test3 REAL,
        average REAL,
        user_id INTEGER
    )
    """)

    conn.commit()
    conn.close()

def add_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        conn.close()
        return True
    except:
        conn.close()
        return False


def get_user(username):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cur.fetchone()

    conn.close()
    return user

def add_student(name, age, t1, t2, t3, user_id):
    avg = round((t1 + t2 + t3) / 3, 2)
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (name, age, test1, test2, test3, average, user_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (name, age, t1, t2, t3, avg, user_id))

    conn.commit()
    conn.close()


def get_students(user_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT * FROM students
        WHERE user_id=?
        ORDER BY average DESC
    """, (user_id,))

    data = cur.fetchall()
    conn.close()
    return data


def delete_student(student_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()