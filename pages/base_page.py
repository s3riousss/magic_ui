import allure
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @staticmethod
    def text_error(act, exp, message):
        return (f"{message}\n"
                f"act_result = {act}\n"
                f"exp_result = {exp}\n")

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
