import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.set_window_size(1920,1080)
    yield browser
    print("\nquit browser..")
    browser.quit()