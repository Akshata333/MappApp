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

@bp.route('/changePassword', methods=('GET', 'POST'))
def changePassword():
    if request.method == 'POST':
        oldpass = request.form['opassword']
        newpass = request.form['npassword']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (g.user['username'],)
        ).fetchone()

        if not check_password_hash(user['password'], oldpass):
            error = 'Incorrect password.'

        if error is None:
            sql = '''UPDATE user
                    SET password = ?
                    WHERE username = ?'''
            cur = db.cursor()
            cur.execute(sql, (generate_password_hash(newpass), user['username']))
            db.commit()

            return redirect(url_for('myAccount.account'))

        flash(error)

    return render_template('myAccount/changePassword.html')