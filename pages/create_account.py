import allure
from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from utils.generate_data import fake_data_for_account
from selenium.webdriver.common.action_chains import ActionChains


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    @allure.step('Fill all element on form create new account')
    def fill_all_form(self, data=fake_data_for_account):
        self.wait_element_presence(10, loc.first_name)
        first_name = self.find(loc.first_name)
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
        self.screenshot()
        btn_create_field.click()
        return fake_data_for_account

    @allure.step('Clik on button "Create an Account"')
    def click_button_create_account(self):
        btn_create_field = self.find(loc.btn_create_account)
        self.wait_element_presence(10, loc.btn_create_account)
        self.driver.execute_script('arguments[0].scrollIntoView(true)', btn_create_field)
        actions = ActionChains(self.driver)
        actions.move_to_element(btn_create_field)
        actions.click()
        actions.perform()
        # btn_create_field.click()

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
