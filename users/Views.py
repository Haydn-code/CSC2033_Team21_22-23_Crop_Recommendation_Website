from flask import Blueprint, render_template, redirect, flash, url_for

from users.Forms import signUpForm, loginForm, searchFarmForm
from flask_login import login_user, logout_user, current_user
from Models import Users, Fields
import bcrypt

users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/', methods=['POST', 'GET'])
@users_blueprint.route('/login', methods=['POST', 'GET'])
def login():
    form = loginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.email.data).first()
        if not bcrypt.checkpw(form.password.data.encode('utf-8'), user.password):
            flash('Incorrect Email/Password')
            return render_template('users/login.html', form=form)
        login_user(user)
        if user.role == 'users':
            return redirect(url_for('users.profile'))
        elif user.role == 'admin':
            return redirect(url_for('users.admin'))
    return render_template('users/login.html', form=form)


@users_blueprint.route('/signUp', methods=['POST', 'GET'])
def signUp():
    from Models import Users
    from Main import db
    form = signUpForm()
    if form.validate_on_submit():
        users = Users.query.filter_by(username=form.email.data).first()
        if users:
            flash('Email already linked to another account')
            return render_template('users/signUp.html', form=form)

        new_user = Users(firstname=form.first_name.data,
                         lastname=form.last_name.data,
                         username=form.email.data,
                         password=form.password.data,
                         phone=form.phone.data,
                         role='users')

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('users/signup.html', form=form)


@users_blueprint.route('/profile', methods=['GET', 'POST'])
def profile():
    from Main import db
    from Models import Fields
    form = searchFarmForm()
    name = current_user.firstname + " " + current_user.lastname
    fields = Fields.query.filter_by(userID=current_user.id)
    display_fields = []
    for field in fields:
        field_dict = {'name': field.name, 'lng': field.longitude, 'lat': field.latitude}
        display_fields.append(field_dict)
    if form.validate_on_submit():
        bounds_chk = False
        if not -180 <= form.longitude.data <= 180 or not -90 <= form.latitude.data <= 90:
            flash("Co-ordinates impossible, ensure it is in the format Longitude Latitude")
            bounds_chk = True
        if Fields and not bounds_chk:
            for field in fields:
                if (field.longitude, field.latitude) == (form.longitude.data, form.latitude.data):
                    flash('Field at that location already stored')
                    bounds_chk = True
                    break
        if not bounds_chk:
            new_field = Fields(longitude=form.longitude.data,
                               latitude=form.latitude.data,
                               name=form.farm_name.data,
                               user=current_user)
            db.session.add(new_field)
            db.session.commit()
        else:
            return render_template('users/profile.html',
                                   form=form,
                                   email=current_user.username,
                                   phone=current_user.phone,
                                   name=name,
                                   fields=display_fields)
    return render_template('users/profile.html',
                           form=form,
                           email=current_user.username,
                           phone=current_user.phone,
                           name=name,
                           fields=display_fields)


@users_blueprint.route('/admin')
def admin():
    id = current_user.id
    return render_template('users/admin.html', id=id)


@users_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('Homepage.homepage'))
