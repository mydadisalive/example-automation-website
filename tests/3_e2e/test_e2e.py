from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    
    fetch_button = browser.find_element(By.ID, 'fetch-quote')
    fetch_button.click()

    # Wait for the quote data to load
    WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'quote'), '"')
    )
    
    quote = browser.find_element(By.ID, 'quote').text
    author = browser.find_element(By.ID, 'author').text
    
    assert quote.startswith('"')
    assert author.startswith('—')

def test_quote_display(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    
    fetch_button = browser.find_element(By.ID, 'fetch-quote')
    fetch_button.click()

    # Wait for the quote and author to be visible
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'quote'))
    )
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'author'))
    )
    
    quote = browser.find_element(By.ID, 'quote').text
    author = browser.find_element(By.ID, 'author').text
    
    assert len(quote) > 0
    assert len(author) > 0
