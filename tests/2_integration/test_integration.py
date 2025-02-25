import requests

def test_homepage():
    response = requests.get('https://mydadisalive.github.io/example-automation-website/')
    assert response.status_code == 200
    assert 'Random Quote App' in response.text

def test_api_response():
    response = requests.get('https://api.quotable.io/random')
    data = response.json()
    
    assert response.status_code == 200
    assert 'content' in data
    assert 'author' in data

# TODO: add a test for multiple requests
