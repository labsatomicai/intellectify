from flask import Blueprint
from ..controllers.forum_controllers import forum_index_page, create_topic_page
forum_blueprint = Blueprint('forum', __name__)

@forum_blueprint.route("/forum", methods=['GET'])
def return_forum():
    return forum_index_page()

@forum_blueprint.route("/create-topic", methods=['GET', 'POST'])
def return_create_topic_page():
    return create_topic_page()
