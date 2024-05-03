from flask import Blueprint
from ..controllers.chat_controllers import mail_index_page, send_message

chat_blueprint = Blueprint('chat', __name__)

@chat_blueprint.route('/mail', methods=['GET', 'POST'])
def return_mail():
    return mail_index_page()

@chat_blueprint.route('/send-message', methods=['GET', 'POST'])
def return_send_message_page():
    return send_message()
