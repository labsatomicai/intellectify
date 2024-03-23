import sqlite3
from flask import render_template, request, redirect, session
from .controllers_methods import check_if_student_logged_in, validate_topic_body
def forum_index_page():
    return render_template('neura_forum.html')

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
