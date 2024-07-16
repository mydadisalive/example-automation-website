import requests

def test_homepage():
    response = requests.get('https://mydadisalive.github.io/example-automation-website/')
    assert response.status_code == 200
    assert 'Random Quote App' in response.text
