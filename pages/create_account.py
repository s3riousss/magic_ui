import allure
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from utils.generate_data import fake_data_for_account
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.project_ec import text_is_not_empty_in_element


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Fill all element on form create new account')
    def fill_all_form(self, data=fake_data_for_account):
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(loc.firs_name))
        first_name = self.find(loc.firs_name)
        last_name = self.find(loc.last_name)
        email_field = self.find(loc.email)
        password_field = self.find(loc.password)
        confirm_password_field = self.find(loc.confirm_password)
        btn_create_field = self.find(loc.btn_create_account)
        first_name.send_keys(data.get('first_name'))
        last_name.send_keys(data.get('last_name'))
        email_field.send_keys(data.get('email'))
        password_field.send_keys(data.get('password'))
        confirm_password_field.send_keys(data.get('password'))
        btn_create_field.click()
        return fake_data_for_account

    @allure.step('Check successful message after create new account')
    def check_alert_text(self, text):
        WebDriverWait(self.driver, 5).until(text_is_not_empty_in_element(loc.alert))
        # alert = self.driver.find_element(*loc.alert_successful)
        alert = self.find(loc.alert)
        assert alert.text == text, self.text_error(alert.text, text, 'Error check alert text')

    # def check_error_message(self):

