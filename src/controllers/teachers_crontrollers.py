import sqlite3
from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from .controllers_methods import validate_username, get_rooms, generate_token


# Teachers signup route
def get_study_areas():
    conn = sqlite3.connect('databases/neurahub-data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, area_name FROM teacher_areas")
    avaliable_study_areas = cursor.fetchall()
    conn.close()

    return avaliable_study_areas

def get_registered_teacher_area(username):
    conn = sqlite3.connect('databases/neurahub-data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT area_id FROM teachers WHERE name = ?", (username,))
    area_id = cursor.fetchone()[0]
    cursor.execute("SELECT area_name FROM teacher_areas WHERE id = ?", (area_id,))
    area_name = cursor.fetchone()[0]
    conn.close()
    return area_name

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
                session['area'] = get_registered_teacher_area(inserted_teacher_username)
                session['logged_in_teacher'] = True
                return redirect('/teacher-panel')

        return "Login failed"
    return render_template('teacher_login.html')


def teacher_panel_page():
    if session.get('logged_in_teacher'):
        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()

        teacher_area = session.get('area')
        print(teacher_area)

        cursor.execute("SELECT id, name FROM teachers WHERE area_id = (SELECT id FROM teacher_areas WHERE area_name = ?)", (teacher_area,))
        teacher_info = cursor.fetchone()

        if not teacher_info:
            return render_template('teacher_panel.html', created_tasks=[])

        teacher_id, teacher_name = teacher_info

        cursor.execute("""
           SELECT tasks.*, rooms.room_name
           FROM tasks
           LEFT JOIN rooms ON tasks.room_id = rooms.id
           WHERE tasks.area_id = ? AND tasks.teacher_id = ?;
           """, (area_id, teacher_id))

        teacher_tasks = cursor.fetchall()

        print(teacher_tasks)

        teacher_tasks_with_room_name = []

        for task in teacher_tasks:
            task_id, task_name, due_date, area_id, room_id, room_name = task

            teacher_tasks_with_room_name.append({
                'task_id': task_id,
                'task_name': task_name,
                'due_date': due_date,
                'area_name': teacher_area,
                'room_name': room_name,
                'teacher_name': teacher_name,
            })

        return render_template('teacher_panel.html', created_tasks=teacher_tasks_with_room_name)
    else:
        return redirect('/teacher-login')


def create_task():
    if session.get('logged_in_teacher'):
        if request.method == 'POST':
            task_name = request.form['task']
            due_date = request.form['due_date']
            area_id = request.form['area-id']
            room_id = request.form['room-id']

            conn = sqlite3.connect('databases/neurahub-data.db')
            cursor = conn.cursor()

            cursor.execute("INSERT INTO tasks (task_name, due_date, area_id, room_id) VALUES (?, ?, ?, ?)", (task_name, due_date, area_id, room_id))
            conn.commit()
            conn.close()


        avaliable_study_areas = get_study_areas()
        avaliable_rooms = get_rooms()
        return render_template('create_task.html', rooms=avaliable_rooms, areas=avaliable_study_areas)

def edit_task(task_id):
    token = generate_token(task_id)
    return redirect(url_for('main.process_edition', token=token))

