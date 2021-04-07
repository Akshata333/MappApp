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

@bp.route('/changeUsername', methods=('GET', 'POST'))
def changeUsername():
    if request.method == 'POST':
        password = request.form['password']
        newuser = request.form['nuser']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (g.user['username'],)
        ).fetchone()

        if not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            sql = '''UPDATE user
                    SET username = ?
                    WHERE username = ?'''
            cur = db.cursor()
            cur.execute(sql, (newuser, g.user['username']))

            cur.execute("SELECT * FROM user")
            rows = cur.fetchall()
            for i in rows:
                print(i["username"], i["password"])

            db.commit()

            return redirect(url_for('myAccount.account'))

        flash(error)

    return render_template('myAccount/changeUsername.html')

@bp.route('/changeSecurityQuestion', methods=('GET', 'POST'))
def changeSecurityQuestion():
    if request.method == 'POST':
        password = request.form['password']
        securityq = request.form['securityq']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (g.user['username'],)
        ).fetchone()

        if not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            sql = '''UPDATE user
                    SET security_question = ?
                    WHERE username = ?'''
            cur = db.cursor()
            cur.execute(sql, (securityq, g.user['username']))
            db.commit()

            return redirect(url_for('myAccount.account'))

        flash(error)

    return render_template('myAccount/changeSecurityQuestion.html')

@bp.route('/forgotPasswordVerified', methods=('GET', 'POST'))
def forgotPasswordVerified():
    if request.method == 'POST':
        username = g.user['username']
        newpass = request.form['newpass']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if error is None:
            sql = '''UPDATE user
                    SET password = ?
                    WHERE username = ?'''
            cur = db.cursor()
            cur.execute(sql, (generate_password_hash(newpass), username))
            db.commit()

            return redirect(url_for('myAccount.account'))

        flash(error)

    return render_template('myAccount/forgotPasswordVerified.html')