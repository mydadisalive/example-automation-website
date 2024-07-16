from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
    yield driver
    driver.quit()

def test_homepage(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    assert 'Weather App' in browser.title

def test_fetch_weather(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    
    city_input = browser.find_element_by_id('city')
    fetch_button = browser.find_element_by_id('fetch-weather')
    
    city_input.send_keys('London')
    fetch_button.click()
    
    # Wait for the weather data to load
    browser.implicitly_wait(10)
    
    temperature = browser.find_element_by_id('temperature').text
    description = browser.find_element_by_id('description').text
    
    assert 'Temperature:' in temperature
    assert 'Description:' in description
