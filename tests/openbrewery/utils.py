ROUTES_LIST = [
    "breweries/meta",
    "breweries/autocomplete",
    "breweries/search",
    "breweries/random",
    "breweries"
]

FILTER_BY_TYPE_LIST = [
    "micro",
    "nano",
    "regional",
    "brewpub",
    "large",  # (deprecated)
    "planning",
    "bar",  # (deprecated)
    "contract",
    "proprietor",
    "closed",
]

existingBrewerieId = "madtree-brewing-cincinnati"


def get_parameter():
    BREWERIES_PARAMETERS = {
        "per_page": "3",
        "by_city": "san_diego",
        "by_dist": "-71.83057593,42.24364875",
        "by_name": "cooper",
        "by_state": "new_york",
        "by_postal": "44107",
        "by_type": "nano",
        "page": "2"
    }
    for key, value in BREWERIES_PARAMETERS.items():
        parameter = {key: value}
        yield parameter


schema_brewery_by_id_positive = {
    "id": {"type": "string"},
    "name": {"type": "string"},
    "brewery_type": {"type": "string"},
    "street": {"type": "string"},
    "address_2": {"type": "null", "nullable": True},
    "address_3": {"type": "null", "nullable": True},
    "city": {"type": "string"},
    "state": {"type": "string"},
    "county_province": {"type": "string"},
    "postal_code": {"type": "string"},
    "country": {"type": "string"},
    "longitude": {"type": "string"},
    "latitude": {"type": "string"},
    "phone": {"type": "string"},
    "website_url": {"type": "string"},
    "updated_at": {"type": "string"},
    "created_at": {"type": "string"}
}

schema_brewery_by_id_negative = {
    "message": {"type": "string", "required": True},

}
