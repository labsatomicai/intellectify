import sqlite3, base64
from flask import render_template, request, redirect, session
from .controllers_methods import check_if_student_logged_in, validate_topic_body

def forum_index_page():
    if check_if_student_logged_in():
        conn = sqlite3.connect('databases/neurahub-data.db')
        cursor = conn.cursor()

        logged_student = session.get("student_username")

        cursor.execute("SELECT room_id FROM students WHERE name =?", (logged_student,))
        room_to_search_content = cursor.fetchone()[0]

        cursor.execute("SELECT post_title, post_body, author, post_image FROM forum_posts WHERE room_id = ?", (room_to_search_content,))
        content = cursor.fetchall()

        conn.close()

        return render_template('neura_forum.html', posts=content)
    else:
        return redirect('/student-login')

def create_topic_page():
    if check_if_student_logged_in():
        if request.method == 'POST':
            conn = sqlite3.connect('databases/neurahub-data.db')
            cursor = conn.cursor()
            topic_title = request.form['topic-name']
            topic_body = request.form['topic-body']
            topic_image = request.files['topic-image']
            print(topic_image)
            topic_author = session.get('student_username')

            cursor.execute("SELECT room_id FROM students WHERE name = ?", (topic_author,))
            room_to_post = cursor.fetchone()[0]
            
            if validate_topic_body(topic_body):
                return "Topic body should be longer"

            if topic_image:
                image_bytes = topic_image.read()
                image_base64_encoded = base64.b64encode(image_bytes).decode('utf-8')
                cursor.execute("INSERT INTO forum_posts (post_title, post_body, author,post_image, room_id) VALUES(?, ?, ?, ?, ?)", (topic_title, topic_body, topic_author, image_base64_encoded, room_to_post))
                conn.commit()
                conn.close()
            else:
                cursor.execute("INSERT INTO forum_posts (post_title, post_body, author, room_id) VALUES (?, ?, ?, ?)", (topic_title, topic_body, topic_author, room_to_post))
                conn.commit()
                conn.close()
        return render_template('create_topic.html')
    else:
        return redirect('/student-login')
