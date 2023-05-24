from flask import Blueprint, render_template, redirect, flash, url_for
from users.Forms import signUpForm, loginForm
from flask_login import login_user, logout_user
from Models import Users
import bcrypt


users_blueprint = Blueprint('users', __name__)
@users_blueprint.route('/', methods=['POST','GET'])
@users_blueprint.route('/login', methods=['POST','GET'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.email.data).first()
        if not bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
            flash('Incorrect Email/Password')
            return render_template('users/login.html', form=form)
        login_user(user)
        return redirect(url_for('users.profile'))
    return render_template('users/login.html', form=form)

@users_blueprint.route('/signUp', methods=['POST', 'GET'])
def signUp():
    from Models import Users
    from main import db
    form = signUpForm()
    if form.validate_on_submit():
        users = Users.query.filter_by(username=form.email.data).first()
        if users:
            flash('Email already linked to another account')
            return render_template('users/signUp.html', form=form)

        new_user = Users(firstname=form.first_name.data,
                         lastname=form.last_name.data,
                         username=form.email.data,
                         password= form.password.data,
                         phone=form.phone.data,
                         role='users')

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/profile')
def profile():
    return render_template('users/profile.html')

@users_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for(''))
