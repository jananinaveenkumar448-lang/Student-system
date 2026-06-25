# Student-system
#  Student Performance Tracker

A Flask-based web application to manage student records, track performance, and export data using CSV.

---

##  Project Overview

The Student Performance Tracker is a simple CRUD web application built using Flask and SQLite.  
It allows users to add, view, and delete student records while also exporting data to a CSV file automatically.

---

##  Features

-  Add student (Name, Age, Score)
-  View all students
-  Leaderboard page (performance ranking)
-  Delete student records
-  Automatic CSV file generation (`students.csv`)
-  Motivational quote API integration
-  Custom 404 and 500 error pages
-  SQLite database storage

---

##  Tech Stack

- Python
- Flask
- SQLite
- HTML / CSS (Bootstrap)
- CSV Module
- Requests (API handling)

---

##  Project Structure
app.py
students.db
students.csv
README.md
models/
templates/
static/
tests/

---

##  Installation & Setup

### 1. Clone the repository
```bash
git clone <your-repo-link>
cd <your-project-folder>
Install dependencies
pip install flask requests
Run the application
python app.py
Open in browser
http://127.0.0.1:5000/
How It Works
User opens the web app
Adds student details (Name, Age, Score)
Data is saved in:
SQLite database (students.db)
CSV file (students.csv)
Students are displayed on homepage and leaderboard
User can delete records anytime
