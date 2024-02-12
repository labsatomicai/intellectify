import sqlite3
from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from .controllers_methods import validate_username, get_rooms

def homepage():
    return render_template('index.html')


# Signup route

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
        cursor.execute("SELECT password, room_id FROM students WHERE name = ?", (inserted_username,))
        stored_password, room_id = cursor.fetchone()
        
        if stored_password:
            if check_password_hash(stored_password, inserted_user_password):
                session['room_id'] = room_id
                return redirect('/assignments')
        else:
            return "Login failed"

    return render_template('login.html')

def students_tasks_panel():
    
    conn = sqlite3.connect('databases/neurahub-data.db')
    cursor = conn.cursor()
    room_id = session.get('room_id')

    if room_id is not None:
        cursor.execute("""
            SELECT tasks.*, teacher_areas.area_name
            FROM tasks
            JOIN teacher_areas ON tasks.area_id = teacher_areas.id
            WHERE tasks.room_id = ?
        """, (room_id,))
        pending_tasks = cursor.fetchall()
        print(pending_tasks)
    conn.close()
    
    return render_template('student_panel.html', tasks=pending_tasks)

