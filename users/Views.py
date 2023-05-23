from flask import Blueprint, render_template, redirect, flash
from users.Forms import signUpForm, loginForm
from Models import Users
from main import db

users_blueprint = Blueprint('users_blueprint', __name__)

@users_blueprint.route('/', methods=['POST','GET'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.email.data)
        if user.password != form.password.data:
            flash('Incorrect Email/Password')
            return render_template('users/login.html', form=form)
        # Login
        return redirect('users.login')
    return render_template('users/login.html', form=form)

@users_blueprint.route('/', methods=['POST', 'GET'])
def signUp():
    form = signUpForm()
    if form.validate_on_submit():

        users = Users.query.filter_by(username=form.email.data)
        if users:
            flash('Email already linked to another account')
            return render_template('users/login.html', form=form)

        new_user = Users(firstname=form.first_name.data,
                         lastname=form.last_name.data,
                         username=form.email.data,
                         password= form.password.data,
                         phone=form.phone.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect('users/login.html')
    return render_template('users/signup.html', form=form)

@users_blueprint.route('/', methods=['POST', 'GET'])
def profile():
    return render_template('users/profile.html')
