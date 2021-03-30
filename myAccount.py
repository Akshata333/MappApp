import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db

bp = Blueprint('myAccount', __name__, url_prefix='/myAccount')

@bp.route('/account', methods=('GET', 'POST'))
def account():
    return render_template('myAccount/myAccount.html')