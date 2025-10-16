from flask import Blueprint, render_template
from flask_login import login_required, current_user
from project import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', first_name=current_user.first_name, last_name=current_user.last_name)

