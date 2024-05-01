from flask import Blueprint
from ..controllers.finder_controllers import get_answer

finder_blueprint = Blueprint('finder', __name__)

@finder_blueprint.route('/finder', methods=['GET', 'POST'])
def return_search():
    return get_answer()