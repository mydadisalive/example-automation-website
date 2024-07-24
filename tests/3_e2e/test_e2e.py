import os
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def save_screenshot(driver, name, save_dir='tests/3_e2e/screenshots'):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, name)
    driver.save_screenshot(file_path)

@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
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
    assert author.startswith('—') or author.startswith('-')  # Check for both em dash and hyphen

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

# TODO: test_fetch_button_clickable(browser):
# TODO: def test_initial_state(browser):
# TODO: test_quote_and_author_update(browser):
# TODO: test_page_contains_elements(browser):
# TODO: test_author_format(browser):
# TODO: test_fetch_quote_error(browser):

def test_fetch_button_clickable(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    fetch_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'fetch-quote'))
    )
    assert fetch_button.is_enabled()
    time.sleep(2)  # Wait for 2 seconds
    save_screenshot(browser, 'fetch_button_clickable.png')
