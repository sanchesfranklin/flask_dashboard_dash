#pylint: disable=import-outside-toplevel, wrong-import-position
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.routes import routes
