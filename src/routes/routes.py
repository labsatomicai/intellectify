from flask import Blueprint
from ..controllers.teachers_crontrollers import teacher_login_page, teacher_signup_page, teacher_panel_page, create_task, edit_task, tokenize_id_for_edition, tokenize_id_to_delete, delete_task
from ..controllers.students_controllers import homepage, signup_page, login_page, students_tasks_panel 

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET'])
def return_index():
    return homepage()

# Students routes
@blueprint.route('/signup', methods=['GET', 'POST'])
def return_signup():
    return signup_page()

@blueprint.route('/login', methods=['GET', 'POST'])
def return_login():
    return login_page()

@blueprint.route('/assignments')
def return_tasks_panel():
    return students_tasks_panel()

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

if __name__ == '__main__':
    blueprint.run(debug=True)
