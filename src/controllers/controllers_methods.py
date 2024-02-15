import re, sqlite3, base64
from flask import session, redirect

def validate_username(username):
    if not (3 <= len(username) <= 20):
        return False

    pattern = re.compile("^[a-zA-Z0-9_-]+$")
    return bool(pattern.match(username))

def get_rooms():
    conn = sqlite3.connect('databases/neurahub-data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, room_name FROM rooms")
    rooms = cursor.fetchall()
    conn.close()

    return rooms

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

def  get_task_by_id(task_id):
    conn = sqlite3.connect('databases/neurahub-data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = cursor.fetchone()
    conn.close
    return task;

def generate_token(task_id):
    id_str = str(task_id).encode('utf-8')
    hashed_id = base64.urlsafe_b64encode(id_str).decode('utf-8')
    return hashed_id

def degenerate_token(token):
    id_bytes = base64.urlsafe_b64decode(token.encode('utf-8'))
    task_id = int(id_bytes)
    return task_id

def check_if_teacher_logged_in():
    if session.get('logged_in_teacher'):
        return True

def check_if_student_logged_in():
    if session.get('student_username'):
        return True
