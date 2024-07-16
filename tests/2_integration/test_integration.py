import requests

def test_homepage():
    response = requests.get('http://example.com')
    assert response.status_code == 200
