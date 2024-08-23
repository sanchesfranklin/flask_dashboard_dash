from flask import render_template, Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')
