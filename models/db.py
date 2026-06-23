import sqlite3

DB = "students.db"


def get_connection():
    return sqlite3.connect(DB)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            score REAL
        )
    """)

    conn.commit()
    conn.close()


def add_student(name, age, score):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO students (name, age, score)
        VALUES (?, ?, ?)
    """, (name, age, score))

    conn.commit()
    conn.close()


def get_all_students():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM students")
    data = cur.fetchall()

    conn.close()
    return data


def delete_student_by_id(student_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()