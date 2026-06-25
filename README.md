Student Performance Tracker
Project Overview

The Student Performance Tracker is a web-based application developed using Flask and SQLite. The main objective of this project is to manage and maintain student records efficiently. It allows users to add, view, and delete student details through a simple web interface. The application stores data permanently using a lightweight SQLite database.

Features
Add new student records with name, age, and score
View all stored student details in a structured format
Delete student records when required
Data persistence using SQLite database
Simple and responsive web interface
Tech Stack
Frontend: HTML, CSS (Flask templates)
Backend: Python (Flask framework)
Database: SQLite
Working Flow

The user opens the web application in a browser and enters student details through a form. Flask processes the request and stores the data in the SQLite database. The stored data is then retrieved and displayed in a table format. Users can also delete records, which updates the database accordingly.

Project Structure
student-tracker/
├── app.py
├── models/
│   └── db.py
├── templates/
│   ├── index.html
│   ├── add_student.html
│   └── students.html
├── static/
│   └── style.css
├── students.db
└── README.md
How to Run
Install Flask
pip install flask
Run the application
python app.py
Open in browser
http://127.0.0.1:5000/
Concepts Used
Flask routing and request handling
HTML templates rendering
SQLite database operations
CRUD operations (Create, Read, Delete)
Form handling in web development
