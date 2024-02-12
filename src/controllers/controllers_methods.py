import re, sqlite3

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
