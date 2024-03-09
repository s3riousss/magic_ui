import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_account import CreateAccount


@pytest.fixture(scope='session')
def start_end():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--log-level=3')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture()
def create_new_account(create_account):
    create_account.open_page()
    data = create_account.fill_all_form()
    return data
