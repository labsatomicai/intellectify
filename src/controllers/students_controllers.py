import sqlite3
from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from .controllers_methods import validate_username, get_rooms, generate_token, check_if_student_logged_in, degenerate_token, get_task_by_id, predict_task_result

# Signup route

def students_signup_page():
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

def students_login_page():
    if check_if_student_logged_in(): 
        return redirect('/assignments')
    else:
        if request.method == 'POST':
            inserted_username = request.form['username']
            inserted_user_password = request.form['password']

            if not  validate_username(inserted_username):
                return redirect('/error')

            if len(inserted_user_password) == 0:
                return redirect('/error')

            conn = sqlite3.connect('databases/neurahub-data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT password, room_id FROM students WHERE name = ?", (inserted_username,))
            stored_password, room_id = cursor.fetchone()
            
            if stored_password:
                if check_password_hash(stored_password, inserted_user_password):
                    session['room_id'] = room_id
                    session['student_username'] = inserted_username
                    return redirect('/assignments')

        return render_template('students_login.html')

def students_tasks_panel():
    if check_if_student_logged_in(): 
        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()
        room_id = session.get('room_id')
        username = session.get('student_username')

        if room_id is not None:
            cursor.execute("""
                           SELECT tasks.id, tasks.task_name, tasks.due_date, tasks.room_id, teacher_areas.area_name
                           FROM tasks
                           JOIN teacher_areas ON tasks.area_id = teacher_areas.id
                           LEFT JOIN feedbacks ON tasks.id = feedbacks.task_id AND feedbacks.student_username = ?
                           WHERE tasks.room_id = ? AND feedbacks.id IS NULL
                           """, (username, room_id))

            pending_tasks = cursor.fetchall()
        conn.close()
        
        return render_template('student_panel.html', tasks=pending_tasks)
    else:
        return redirect('/student-login')

def tokenize_id_for_rating(task_id):
    if check_if_student_logged_in():
        token = generate_token(task_id)
        return redirect(url_for('main.return_task_rating', token=token))
    else:
        return redirect('/student-login')

def rate_task(token):
    if check_if_student_logged_in():
        task_id_to_be_reviewed = degenerate_token(token)
        task_to_review = get_task_by_id(task_id_to_be_reviewed)
        
        if task_to_review:
            if request.method == 'POST':
                user_satisfaction = request.form['ov-satisfaction']
                user_clarity = request.form['clarity-relevance']
                user_resources = request.form['resources']
                user_learning_exp = request.form['learning']
                user_improvements = request.form['improvements']

                user_numbered_rating  = float(request.form['grade'])
                rating_result = predict_task_result(user_numbered_rating)

                username = session.get('student_username')

                conn = sqlite3.connect('databases/neurahub-data.db')
                cursor = conn.cursor()

                cursor.execute("""
                INSERT INTO feedbacks (task_id, student_username, satisfaction, clarity, resources, learning_exp, improvements, numbered_rating, rating_result) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (task_id_to_be_reviewed, session['student_username'], user_satisfaction, user_clarity, user_resources, user_learning_exp, user_improvements, user_numbered_rating, rating_result))

                conn.commit()
                conn.close()

        return render_template('rate_task.html', task=task_to_review)
    else:
        return redirect('/student-login')


