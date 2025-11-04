from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, logout_user
from werkzeug.security import generate_password_hash
from project import db
from project.models import User
import pycountry
from project.utils.countries import get_subdivisions, get_country_calling_codes
from config import Config

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html',
        first_name=current_user.first_name,
        last_name=current_user.last_name
    )


@main.route('/profile/edit', methods=['GET', 'POST'])
@login_required
def edit_profile():
    if request.method == 'POST':
        # Get form values
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        title = request.form.get('title')
        company_name = request.form.get('company_name')
        street_address = request.form.get('street_address')
        street_address_line2 = request.form.get('street_address_line2')
        city = request.form.get('city')
        state_province_region = request.form.get('state_province_region')
        postal_code = request.form.get('postal_code')
        country = request.form.get('country')
        country_code = request.form.get('country_code')
        phone = request.form.get('phone')
        phone_type = request.form.get('phone_type')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Update basic profile fields
        current_user.first_name = first_name
        current_user.last_name = last_name
        current_user.title = title
        current_user.company_name = company_name
        current_user.street_address = street_address
        current_user.street_address_line2 = street_address_line2
        current_user.city = city
        current_user.state_province_region = state_province_region
        current_user.postal_code = postal_code
        current_user.country = country
        current_user.country_code = country_code
        current_user.phone = phone
        current_user.phone_type = phone_type

        # Track if password was changed
        password_changed = False

        # Handle password update only if both fields are filled
        if password or confirm_password:
            if password != confirm_password:
                flash("Passwords do not match.", "danger")
                return redirect(url_for('main.edit_profile'))
            if password.strip() == "":
                flash("Password cannot be empty.", "danger")
                return redirect(url_for('main.edit_profile'))
            current_user.password = generate_password_hash(password, method='pbkdf2:sha256')
            password_changed = True

        db.session.commit()

        if password_changed:
            flash('Profile updated successfully! Please log in again with your new password.', 'success')
            logout_user()
            return redirect(url_for('auth.login'))

        flash('Profile updated successfully!', 'success')
        return redirect(url_for('main.profile'))

    # Preload data for form rendering
    countries = [(c.alpha_2, c.name) for c in pycountry.countries]
    countries_phone = get_country_calling_codes()
    subdivisions = get_subdivisions()

    return render_template(
        'edit_profile.html',
        user=current_user,
        countries=countries,
        countries_phone=countries_phone,
        subdivisions=subdivisions,
        google_places_api_key=Config.GOOGLE_PLACES_API_KEY
    )
