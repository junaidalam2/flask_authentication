from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    # Required personal and business info
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    company_name = db.Column(db.String(300), nullable=False)

    # Required address fields (international-friendly)
    country = db.Column(db.String(100), nullable=False)
    street_address = db.Column(db.String(200), nullable=False)
    street_address_line2 = db.Column(db.String(200))  # optional
    city = db.Column(db.String(100), nullable=False)
    state_province_region = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)

    # Required contact info
    phone = db.Column(db.String(20), nullable=False)
    phone_type = db.Column(db.String(20), nullable=False)  # e.g., "mobile", "work", "home"

    def __repr__(self):
        return f"<User {self.email}>"