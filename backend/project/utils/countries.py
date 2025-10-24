import pycountry
import phonenumbers

def get_country_calling_codes():
    countries = []
    for country in pycountry.countries:
        try:
            dial_code = phonenumbers.country_code_for_region(country.alpha_2)
            if dial_code:  # skip invalid or missing ones
                countries.append({
                    "name": country.name,
                    "alpha_2": country.alpha_2,
                    "dial_code": f"+{dial_code}"
                })
        except Exception:
            continue  # skip unrecognized territories

    # Priority countries first
    priority = ['US', 'CA', 'GB']
    countries.sort(key=lambda c: (
        0 if c["alpha_2"] in priority else 1,
        priority.index(c["alpha_2"]) if c["alpha_2"] in priority else c["name"]
    ))
    return countries


def get_subdivisions():
    subdivisions_dict = {}
    for subdivision in pycountry.subdivisions:
        country_code = subdivision.country_code
        subdivisions_dict.setdefault(country_code, []).append({
            "code": subdivision.code,
            "name": subdivision.name
        })
    return subdivisions_dict