import pycountry
import phonenumbers

def get_country_calling_codes():
    countries = []
    for country in pycountry.countries:
        try:
            dial_code = phonenumbers.country_code_for_region(country.alpha_2)
            countries.append({
                "name": country.name,
                "alpha_2": country.alpha_2,
                "dial_code": f"+{dial_code}"
            })
        except Exception:
            # skip regions without phone codes (e.g. Antarctica)
            continue
    # Optional: sort alphabetically
    countries.sort(key=lambda x: x["name"])
    return countries


def get_subdivisions():
    subdivisions_dict = {}
    for subdivision in pycountry.subdivisions:
        country_name = pycountry.countries.get(alpha_2=subdivision.country_code).name
        subdivisions_dict.setdefault(country_name, []).append({
            "code": subdivision.code,
            "name": subdivision.name
        })
    return subdivisions_dict