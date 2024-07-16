from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
    yield driver
    driver.quit()

def test_homepage(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    assert 'Example Automation Website' in browser.title

def test_contact_form(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    name_input = browser.find_element_by_id('name')
    email_input = browser.find_element_by_id('email')
    submit_button = browser.find_element_by_css_selector('input[type="submit"]')
    
    name_input.send_keys('John Doe')
    email_input.send_keys('john@example.com')
    submit_button.click()
    
    response_text = browser.find_element_by_id('form-response').text
    assert 'Thank you, John Doe! We will contact you at john@example.com.' in response_text

def test_fetch_repos(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    username_input = browser.find_element_by_id('github-username')
    fetch_button = browser.find_element_by_id('fetch-repos')
    
    username_input.send_keys('mydadisalive')
    fetch_button.click()
    
    # Wait for the repositories to be fetched and displayed
    browser.implicitly_wait(10)
    repo_list_items = browser.find_elements_by_css_selector('#repo-list li')
    assert len(repo_list_items) > 0
