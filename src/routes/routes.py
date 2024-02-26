from flask import Blueprint, render_template, redirect, url_for
from ..controllers.teachers_crontrollers import teacher_login_page, teacher_signup_page, teacher_panel_page, create_task, edit_task, tokenize_id_for_edition, tokenize_id_to_delete, delete_task, tokenize_id_for_feedback, get_feedback
from ..controllers.students_controllers import students_signup_page, students_login_page , students_tasks_panel , tokenize_id_for_rating, rate_task
from ..controllers.controllers_methods import log_out

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET'])
def return_index():
    return render_template('index.html')

@blueprint.route('/access', methods=['GET'])
def return_access():
    return render_template('login_panel.html')

@blueprint.route('/success', methods=['GET', 'POST'])
def return_success():
    return render_template('success.html')

@blueprint.route('/error', methods=['GET'])
def return_error():
    return render_template('error.html')

@blueprint.route('/logout-student', methods=['GET'])
def logout_student():
    log_out('student_username')
    return redirect('/')

@blueprint.route('/logout-teacher', methods=['GET'])
def logout_teacher():
    log_out('logged_in_teacher')
    return redirect('/')

# Students routes

@blueprint.route('/student-signup', methods=['GET', 'POST'])
def return_signup():
    return students_signup_page()

@blueprint.route('/student-login', methods=['GET', 'POST'])
def return_login():
    return students_login_page()

@blueprint.route('/assignments')
def return_tasks_panel():
    return students_tasks_panel()

@blueprint.route('/rate-process-id/<int:task_id>', methods=['GET'])
def return_processed_id_to_rate(task_id):
    return tokenize_id_for_rating(task_id)

@blueprint.route('/rate-task/<token>', methods=['GET', 'POST'])
def return_task_rating(token):
    return rate_task(token)

# Teachers router

@blueprint.route('/teacher-signup', methods=['GET', 'POST'])
def return_teacher_signup():
    return teacher_signup_page()

@blueprint.route('/teacher-login', methods=['GET', 'POST'])
def return_login_page():
    return teacher_login_page()

@blueprint.route('/teacher-panel', methods=['GET', 'POST'])
def return_teacher_panel():
    return teacher_panel_page()

@blueprint.route('/create-task', methods=['GET', 'POST'])
def return_create_task():
    return create_task()

@blueprint.route('/edit-process-id/<int:task_id>', methods=['GET'])
def return_processed_id_to_edit(task_id):
    return tokenize_id_for_edition(task_id)

@blueprint.route('/edit-task/<token>', methods=['GET', 'POST'])
def return_task_edition(token):
    return edit_task(token)

@blueprint.route('/delete-process-id/<int:task_id>', methods=['GET'])
def return_processed_id_to_delete(task_id):
    return tokenize_id_to_delete(task_id)

@blueprint.route('/delete-task/<token>')
def return_task_deletion(token):
    return delete_task(token)

@blueprint.route('/feedback-process-id/<int:task_id>', methods=['GET'])
def return_processed_id_to_feedback(task_id):
    return tokenize_id_for_feedback(task_id)

@blueprint.route('/feedback/<token>')
def return_task_feedback(token):
    return get_feedback(token)

if __name__ == '__main__':
    blueprint.run(debug=True)
