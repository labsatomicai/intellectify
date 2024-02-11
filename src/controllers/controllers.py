from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3, re

def homepage():
    return render_template('index.html')

def validate_username(username):
    if not (3 <= len(username) <= 20):
        return False

    pattern = re.compile("^[a-zA-Z0-9_-]+$")
    return bool(pattern.match(username))

# Signup route

def get_rooms():
    conn = sqlite3.connect('databases/neurahub-data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, room_name FROM rooms")
    rooms = cursor.fetchall()
    conn.close()

    return rooms

def signup_page():
    if request.method == 'POST':
        username = request.form['username']
        raw_user_password = request.form['password']
        room_id = request.form['room-id']

        if not validate_username(username):
            return "Invalid nickname"

        hashed_user_password = generate_password_hash(raw_user_password)

        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, password, room_id) VALUES (?, ?, ?)", (username, hashed_user_password, room_id))
        conn.commit()
        conn.close()

        return redirect('/')

    rooms = get_rooms()
    return render_template('signup.html', rooms=rooms)

# Login route

def login_page():
    if request.method == 'POST':
        inserted_username = request.form['username']
        inserted_user_password = request.form['password']

        if not  validate_username(inserted_username):
            return "Invalidad username"

        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM students WHERE name = ?", (inserted_username,))
        stored_password = cursor.fetchone()

        if stored_password:
            if check_password_hash(stored_password[0], inserted_user_password):
                return redirect('/')

        return "Login failed"

    return render_template('login.html')

# Teachers signup route
def get_study_areas():
    conn = sqlite3.connect('databases/neurahub-data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, area_name FROM teacher_areas")
    areas = cursor.fetchall()
    conn.close()

    return areas

def teacher_signup_page():
    if request.method == 'POST':
        teacher_username = request.form['username']
        raw_teacher_password = request.form['password']
        area_id = request.form['area-id']

        if not validate_username(teacher_username):
            return "Invalid nickname"

        hashed_teacher_password = generate_password_hash(raw_teacher_password)

        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teachers (name, password, area_id) VALUES (?, ?, ?)", (teacher_username, hashed_teacher_password, area_id))
        conn.commit()
        conn.close()
        
        return redirect('/')

    study_areas = get_study_areas()
    return render_template('teacher_signup.html', areas=study_areas)

def teacher_login_page():
    if request.method == 'POST':
        inserted_teacher_username = request.form['username']
        inserted_teacher_password = request.form['password']

        if not validate_username(inserted_teacher_username):
            return "Invalid username"
        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM teachers WHERE name = ?", (inserted_teacher_username,))
        stored_password = cursor.fetchone()

        if stored_password:
            if check_password_hash(stored_password[0], inserted_teacher_password):
                return redirect('/')

        return "Login failed"

    return render_template('teacher_login.html')
