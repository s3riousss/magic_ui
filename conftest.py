import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_account import CreateAccount
from pages.eco_friendly import EcoFriendly
from pages.sale import Sale


@pytest.fixture(scope='session')
def start_end():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    # options.add_argument('start-maximized')
    options.add_argument('window-size=1920,1080')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--log-level=3')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture()
def create_new_account(create_account):
    create_account.open_page()
    data = create_account.fill_all_form()
    return data


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale_page(driver):
    return Sale(driver)
