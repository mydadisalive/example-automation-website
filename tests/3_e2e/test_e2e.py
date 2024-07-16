from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
    yield driver
    driver.quit()

def test_homepage(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    assert 'Random Quote App' in browser.title

def test_fetch_quote(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    
    fetch_button = browser.find_element_by_id('fetch-quote')
    fetch_button.click()
    
    # Wait for the quote data to load
    browser.implicitly_wait(10)
    
    quote = browser.find_element_by_id('quote').text
    author = browser.find_element_by_id('author').text
    
    assert quote.startswith('"')
    assert author.startswith('—')
