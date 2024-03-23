import sqlite3
from flask import render_template, request, redirect, session
from .controllers_methods import validate_username, hash_pass, check_pass, check_if_admin_logged_in, get_tasks, get_rooms, get_study_areas

def admin_signup_page():
    if request.method == 'POST':
        admin_username = request.form['admin-username']
        raw_admin_password = request.form['admin-password']

        if not validate_username(admin_username):
            return redirect('/error')

        hashed_admin_password = hash_pass(raw_admin_password)

        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO admin_info (username, password) VALUES (?, ?)", (admin_username, hashed_admin_password))
        conn.commit()
        conn.close()
        
    return render_template('admin_signup.html')

def admin_login_page():
    if request.method == 'POST':
        inserted_admin_username = request.form['admin-username']
        inserted_admin_password = request.form['admin-password']
        
        if not validate_username(inserted_admin_username):
            return redirect('/error')
        
        if len(inserted_admin_password) == 0:
            return redirect ('/error')
    
        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM admin_info WHERE username = ?", (inserted_admin_username,))
        stored_password = cursor.fetchone()[0]
        print(stored_password)
    
        if stored_password:
            if check_pass(stored_password, inserted_admin_password):
                session['logged_in_adm'] = True
                session['admin_username'] = inserted_admin_username
                return redirect('/admin-panel')

    return render_template('admin_login.html')

def admin_panel_page():
    if check_if_admin_logged_in():
        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()
        #The difference to the teachers is, the admin can see the student name in the feedback card
        cursor.execute("""
            SELECT tasks.id, tasks.task_name, tasks.due_date, rooms.room_name, teacher_areas.area_name, tasks.teacher_username
            FROM tasks
            LEFT JOIN rooms ON tasks.room_id = rooms.id
            LEFT JOIN teacher_areas ON tasks.area_id = teacher_areas.id
        """)
    
        created_tasks = cursor.fetchall()
        conn.close()
    
        task_summary = []
    
        for task in created_tasks:
            print(task)
            task_id, task_name, due_date, study_area, room_name, responsible_teacher = task
    
            task_summary.append({
                'task_id': task_id,
                'task_name': task_name,
                'due_date': due_date,
                'area_name': study_area,
                'room_name': room_name,
                'responsible_teacher': responsible_teacher
            })        
        return render_template('admin_panel.html', current_tasks=task_summary)
    else:
        return redirect('/')
