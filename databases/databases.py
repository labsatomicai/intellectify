import sqlite3

conn = sqlite3.connect('neurahub-data.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        room_name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        room_id INTEGER NOT NULL,
        FOREIGN KEY (room_id) REFERENCES room (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS teacher_areas (
        id INTEGER PRIMARY KEY,
        area_name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE teachers (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        area_id INTEGER NOT NULL,
        FOREIGN KEY (area_id) REFERENCES teacher_areas (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        task_name TEXT NOT NULL,
        due_data TEXT NOT NULL,
        area TEXT NOT NULL,
        room_id INTEGER NOT NULL,
        teacher_id INTEGER NOT NULL,
        FOREIGN KEY (room_id) REFERENCES rooms (id),
        FOREIGN KEY (teacher_id) REFERENCES teachers (id)
    )
''')

conn.commit()
conn.close()
