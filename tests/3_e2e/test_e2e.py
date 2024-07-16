from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH
    yield driver
    driver.quit()

def test_homepage(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    assert 'Trivia Quiz' in browser.title

def test_quiz_functionality(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    
    # Wait for the question to load
    browser.implicitly_wait(10)
    
    # Select an answer
    answers = browser.find_elements_by_name('answer')
    if answers:
        answers[0].click()
    
    # Submit the form
    submit_button = browser.find_element_by_css_selector('input[type="submit"]')
    submit_button.click()
    
    # Check feedback
    feedback = browser.find_element_by_id('feedback')
    assert feedback.text in ['Correct!', 'Wrong! The correct answer was: ']

def test_new_question_button(browser):
    browser.get('https://mydadisalive.github.io/example-automation-website/')
    
    # Wait for the question to load
    browser.implicitly_wait(10)
    
    initial_question = browser.find_element_by_id('question').text
    
    new_question_button = browser.find_element_by_id('new-question')
    new_question_button.click()
    
    # Wait for the new question to load
    browser.implicitly_wait(10)
    
    new_question = browser.find_element_by_id('question').text
    
    assert initial_question != new_question
