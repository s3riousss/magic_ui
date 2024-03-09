import allure
import inspect
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.project_ec import text_is_not_empty_in_element
from pages.locators import create_account_locators as loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @staticmethod
    def assert_check(act_result, exp_result, message):
        stack = inspect.stack()
        name_function = stack[1].function
        print(f'Start checking: {name_function}')
        print(f'Actual result= {act_result}\n')
        print(f'Expected result= {exp_result}\n')
        assert act_result == exp_result, f'\n{message}\n' \
                                         f'Actual_result = {act_result}\n' \
                                         f'Expected_result = {exp_result}\n'
        print(f'Done checking: {name_function}')

    def wait_element_presence(self, timeout, locator):
        return WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located(locator))

    def wait_element_text(self, timeout, locator):
        return WebDriverWait(self.driver, timeout).until(text_is_not_empty_in_element(locator))

    @allure.step('Open page for test ')
    def open_page(self, delete_cookies=None):
        if delete_cookies:
            self.driver.delete_all_cookies()
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    @allure.step('Checking successful message after create new account')
    def check_alert_text(self, text):
        self.wait_element_text(5, loc.alert)
        alert = self.find(loc.alert)
        assert alert.text == text, self.assert_check(alert.text, text, 'Error check alert text')

    @allure.step('Checking error message for field')
    def check_error_message(self, field, exp_error):
        match field:
            case 'first_name':
                first_name_error = self.find(loc.first_name_error)
                self.assert_check(
                    first_name_error.text, exp_error, f'Error check {field}'
                )
            case 'last_name':
                last_name_error = self.find(loc.last_name_error)
                assert last_name_error.text == exp_error, self.assert_check(
                    last_name_error.text, exp_error, f'Error check {field}'
                )
            case 'email':
                email_field_error = self.find(loc.email_error)
                self.assert_check(
                    email_field_error.text, exp_error, f'Error check {field}'
                )
            case 'email':
                email_field_error = self.find(loc.email_error)
                self.assert_check(
                    email_field_error.text, exp_error, f'Error check {field}'
                )
            case 'password_':
                password_field_error = self.find(loc.password_error)
                self.assert_check(
                    password_field_error.text, exp_error, f'Error check {field}'
                )
            case 'confirm_password':
                confirm_password_field = self.find(loc.confirm_password_error)
                self.assert_check(
                    confirm_password_field.text, exp_error, f'Error check {field}'
                )
