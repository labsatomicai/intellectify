import re, sqlite3
import hashlib

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

def generate_token(task_id):
    id_str = str(task_id)
    print(id_str)
    hashed_id = hashlib.sha256(id_str.encode('utf-8')).hexdigest()
    return hashed_id
