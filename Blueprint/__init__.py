from flask import Blueprint

bp = Blueprint('bp', __name__, template_folder='templates')

from Blueprint import routes
