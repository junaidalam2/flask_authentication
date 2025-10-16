from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from .models import User
from project import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    title = request.form.get('title')
    company_name = request.form.get('company_name')
    country = request.form.get('country')
    street_address = request.form.get('street_address')
    street_address_line2 = request.form.get('street_address_line2')
    city = request.form.get('city')
    state_province_region = request.form.get('state_province_region')
    postal_code = request.form.get('postal_code')
    phone = request.form.get('phone')
    phone_type = request.form.get('phone_type')

    user = User.query.filter_by(email=email).first()

    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            title=title, 
            company_name=company_name, 
            country=country, 
            street_address=street_address, 
            street_address_line2=street_address_line2, 
            city=city, 
            state_province_region=state_province_region, 
            postal_code=postal_code, 
            phone=phone, 
            phone_type=phone_type, 
            password=generate_password_hash(password, method='sha256')
            )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))