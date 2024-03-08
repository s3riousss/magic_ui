from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_click_button_with_all_correct_fields(create_account):
    create_account.open_page()
    create_account.fill_all_form()
