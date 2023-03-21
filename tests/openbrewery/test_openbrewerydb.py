import cerberus
import pytest
import requests

from utils import *


@pytest.mark.smoke
@pytest.mark.parametrize("routs", ROUTES_LIST)
def test_get_routs(routs, openbrewerydb_url):
    """Test all routs from the ROUTES_LIST on tests.openbrewery.utils for availability"""
    response = requests.get(openbrewerydb_url + routs)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"


@pytest.mark.smoke
@pytest.mark.parametrize("breweries_parameter", get_parameter())
def test_breweries_parameters(breweries_parameter, openbrewerydb_url):
    """Test all breweries parameters from the ROUTES_LIST on tests.openbrewery.utils for availability"""
    response = requests.get(f"{openbrewerydb_url}breweries", params=breweries_parameter)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"


@pytest.mark.smoke
@pytest.mark.parametrize("filter_by_type", FILTER_BY_TYPE_LIST)
def test_filter_by_type(filter_by_type, openbrewerydb_url):
    """Test all parameters from the FILTER_BY_TYPE_LIST on tests.openbrewery.utils for availability"""
    by_type_parameters = {"by_type": filter_by_type}
    response = requests.get(openbrewerydb_url + "breweries", params=by_type_parameters)
    assert response.status_code == 200
    assert response.headers['Content-Type'] == "application/json; charset=utf-8"


@pytest.mark.smoke
def test_get_breweries_by_id_positive(openbrewerydb_url):
    """Get exact brewery by id - positive case: existing id """
    response = requests.get(openbrewerydb_url + "breweries/madtree-brewing-cincinnati")
    v = cerberus.Validator()
    assert response.status_code == 200


@pytest.mark.regress
def test_get_breweries_by_id_negative(openbrewerydb_url):
    """Get exact brewery by id - negative case: not existing id """
    response = requests.get(openbrewerydb_url + "breweries/notExistingId")
    v = cerberus.Validator()
    assert response.status_code == 404
    assert v.validate(response.json(), schema_brewery_by_id_negative)
    assert response.json() == {"message": "Couldn't find Brewery"}
