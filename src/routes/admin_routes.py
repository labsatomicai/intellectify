from flask import Blueprint
from ..controllers.admin_controllers import admin_login_page, admin_signup_page, admin_panel_page

admins_blueprint = Blueprint('admin', __name__)

@admins_blueprint.route('/admin-login', methods=['GET', 'POST'])
def return_admin_login_page():
    return admin_login_page()

@admins_blueprint.route('/admin-signup', methods=['GET', 'POST'])
def return_admin_signup_page():
    return admin_signup_page()

@admins_blueprint.route('/admin-panel', methods=['GET', 'POST'])
def return_admin_panel():
    return admin_panel_page()