import time

import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    time.sleep(3)
