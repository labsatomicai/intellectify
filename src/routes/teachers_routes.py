from flask import Blueprint
from ..controllers.teachers_crontrollers import teacher_login_page, teacher_signup_page, teacher_panel_page, create_task, edit_task, tokenize_id_for_edition, tokenize_id_to_delete, delete_task, tokenize_id_for_feedback, get_feedback

teachers_blueprint = Blueprint('teachers', __name__)

@teachers_blueprint.route('/teacher-signup', methods=['GET', 'POST'])
def return_teacher_signup():
    return teacher_signup_page()

@teachers_blueprint.route('/teacher-login', methods=['GET', 'POST'])
def return_login_page():
    return teacher_login_page()

@teachers_blueprint.route('/teacher-panel', methods=['GET', 'POST'])
def return_teacher_panel():
    return teacher_panel_page()

@teachers_blueprint.route('/create-task', methods=['GET', 'POST'])
def return_create_task():
    return create_task()

@teachers_blueprint.route('/edit-process-id/<int:task_id>', methods=['GET'])
def return_processed_id_to_edit(task_id):
    return tokenize_id_for_edition(task_id)

@teachers_blueprint.route('/edit-task/<token>', methods=['GET', 'POST'])
def return_task_edition(token):
    return edit_task(token)

@teachers_blueprint.route('/delete-process-id/<int:task_id>', methods=['GET'])
def return_processed_id_to_delete(task_id):
    return tokenize_id_to_delete(task_id)

@teachers_blueprint.route('/delete-task/<token>')
def return_task_deletion(token):
    return delete_task(token)

@teachers_blueprint.route('/feedback-process-id/<int:task_id>', methods=['GET'])
def return_processed_id_to_feedback(task_id):
    return tokenize_id_for_feedback(task_id)

@teachers_blueprint.route('/feedback/<token>')
def return_task_feedback(token):
    return get_feedback(token)
