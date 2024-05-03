from flask import Blueprint, render_template, redirect, url_for
from .teachers_routes import teachers_blueprint
from .students_routes import students_blueprint
from .admin_routes import admins_blueprint
from .forum_routes import forum_blueprint
from .finder_routes import finder_blueprint
from .chat_routes import chat_blueprint
from ..controllers.controllers_methods import log_out

blueprint = Blueprint('main', __name__)

#Non-specific routes

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


blueprint.register_blueprint(teachers_blueprint)
blueprint.register_blueprint(students_blueprint)
blueprint.register_blueprint(admins_blueprint)
blueprint.register_blueprint(forum_blueprint)
blueprint.register_blueprint(finder_blueprint)
blueprint.register_blueprint(chat_blueprint)

if __name__ == '__main__':
    blueprint.run(debug=True)
