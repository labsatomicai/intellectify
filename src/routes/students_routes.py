from flask import Blueprint
from ..controllers.students_controllers import students_signup_page, students_login_page , students_tasks_panel , tokenize_id_for_rating, rate_task

students_blueprint = Blueprint('students', __name__)

@students_blueprint.route('/student-signup', methods=['GET', 'POST'])
def return_signup():
    return students_signup_page()

@students_blueprint.route('/student-login', methods=['GET', 'POST'])
def return_login():
    return students_login_page()

@students_blueprint.route('/assignments')
def return_tasks_panel():
    return students_tasks_panel()

@students_blueprint.route('/rate-process-id/<int:task_id>', methods=['GET'])
def return_processed_id_to_rate(task_id):
    return tokenize_id_for_rating(task_id)

@students_blueprint.route('/rate-task/<token>', methods=['GET', 'POST'])
def return_task_rating(token):
    return rate_task(token)
