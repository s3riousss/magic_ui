import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.create_account import CreateAccount


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('start-maximized')
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    time.sleep(5)


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)
