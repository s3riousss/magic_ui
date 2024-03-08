from pages.base_page import BasePage
from pages.locators import create_account_locators as loc
from utils.generate_data import fake_data_for_account


class CreateAccount(BasePage):
    page_url = '/customer/account/create/'

    def fill_all_form(self):
        first_name = self.find(loc.firs_name)
        last_name = self.find(loc.last_name)
        email_field = self.find(loc.email)
        password_field = self.find(loc.password)
        confirm_password_field = self.find(loc.confirm_password)
        btn_create_field = self.find(loc.btn_create_account)
        first_name.send_keys(fake_data_for_account.get('first_name'))
        last_name.send_keys(fake_data_for_account.get('last_name'))
        email_field.send_keys(fake_data_for_account.get('email'))
        password_field.send_keys(fake_data_for_account.get('password'))
        confirm_password_field.send_keys(fake_data_for_account.get('password'))
        btn_create_field.click()
