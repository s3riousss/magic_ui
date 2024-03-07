from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_click_button_empty_fields(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/create/')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'submit')))
    button_submit = driver.find_element(By.CLASS_NAME, 'submit')
    button_submit.submit()
