import sqlite3
from flask import render_template, request, redirect, session
from .controllers_methods import check_if_student_logged_in, validate_topic_body

def forum_index_page():
    if check_if_student_logged_in():
        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()

        # The forum is working based on the room id select from the database using the student registered username
        logged_student = session.get("student_username")

        cursor.execute("SELECT room_id FROM students WHERE name =?", (logged_student,))
        room_to_search_content = cursor.fetchone()[0]

        cursor.execute("SELECT post_title, post_body, author FROM forum_posts WHERE room_id = ?", (room_to_search_content,))
        content = cursor.fetchall()
        print(content)
    return render_template('neura_forum.html', posts=content)

def create_topic_page():
    if check_if_student_logged_in():
        if request.method == 'POST':
            topic_title = request.form['topic-name']
            topic_body = request.form['topic-body']

            if validate_topic_body(topic_body):
                return "Topic body should be longer"

            conn = sqlite3.connect('databases/neurahub-data.db')
            cursor = conn.cursor()

            topic_author = session.get('student_username')

            cursor.execute("SELECT room_id FROM students WHERE name = ?", (topic_author,))

            room_to_post = cursor.fetchone()[0]
            
            print(topic_title, topic_body, topic_author, room_to_post)

            cursor.execute("INSERT INTO forum_posts (post_title, post_body, author, room_id) VALUES (?, ?, ?, ?)", (topic_title, topic_body, topic_author, room_to_post))
            conn.commit()
            conn.close()
        return render_template('create_topic.html')
    else:
        return redirect('/student-login')
