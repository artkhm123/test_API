<h1>API_testing</h1>

This repository is created with a purpose of API testing practice and practice of parametrisation with the help
of pytest_addoption.

Testing following APIs:

1) https://dog.ceo/dog-api/
2) https://www.openbrewerydb.org/
3) https://jsonplaceholder.typicode.com/
4) pytest_addoption practice

<h2>Each API is tested in separate suit in separate directory:</h2>

1) tests/openbrewery
2) tests/jsonplaceholder
3) tests/dog_ceo
4) tests/addoption_practice

<h2>To run each suit with default url settings execute:</h2>

1) pytest -v tests/openbrewery/test_openbrewerydb.py
2) pytest -v tests/jsonplaceholder/test_jsonplaceholder.py
3) pytest -v tests/dog_ceo/test_dog_ceo.py
4) pytest -v tests/addoption_practice/test_parameter.py

<h2>Parameters for testing API (suits 1,2,3):</h2>
<p>--url -> url to execute</p>
<p>-m -> marks</p>
<p>smoke : this mark is for smoke run</p>
<p>regress : this is for regress ran</p>
<p>xfail: known failed tests</p>


<h2>Parameters for addoption_practice:</h2>
<p>--url -> url to execute</p>
<p>--status_code -> expected status code</p>