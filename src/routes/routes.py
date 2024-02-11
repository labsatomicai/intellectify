from flask import Blueprint
from ..controllers.controllers import homepage, signup_page, login_page, teacher_signup_page, teacher_login_page

blueprint = Blueprint('main', __name__)

@blueprint.route('/', methods=['GET'])
def return_index():
    return homepage()

@blueprint.route('/signup', methods=['GET', 'POST'])
def return_signup():
    return signup_page()

@blueprint.route('/login', methods=['GET', 'POST'])
def return_login():
    return login_page()

@blueprint.route('/teacher-signup', methods=['GET', 'POST'])
def return_teacher_signup():
    return teacher_signup_page()

@blueprint.route('/teacher-login', methods=['GET', 'POST'])

def return_login_page():
    return teacher_login_page()

if __name__ == '__main__':
    blueprint.run(debug=True)
