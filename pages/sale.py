from pages.base_page import BasePage
from pages.locators import sele_locators as loc


class Sale(BasePage):
    page_url = '/sale.html'
    page_women_url = '/women-sale.html'
    page_men_bargains = 'promotions/men-sale.html'
    page_gear = 'gear.html'

    def check_click_button_url_women(self):
        button_women_shop = self.driver.find_element(*loc.shop_women_deals)
        button_women_shop.click()
        self.wait_full_to_load()
        current_url = self.driver.current_url
        assert self.page_women_url in current_url, f'Error page {self.page_women_url} not found'


    def check_men_bargains(self):
        bargains = self.driver.find_element(*loc.men_bargains)
        bargains.click()
        self.wait_full_to_load()
        current_url = self.driver.current_url
        assert self.page_men_bargains in current_url, f'Error page {self.page_women_url} not found'


    def luma_gear_steals(self):
        luma = self.driver.find_element(*loc.luma_gear_steals)
        self.title = luma.find_element(*loc.title).text
        self.info = luma.find_element(*loc.info).text
        self.more_icon = luma.find_element(*loc.more_icon).text
        # self.assert_check(text[0], exp_title, 'Error check title\n')
        # self.assert_check(text[1], exp_message, 'Error check message\n')
        print(f'text={self.info}')
        luma.click()
        current_url = self.driver.current_url
        assert self.page_gear in current_url, f'Error page {self.page_women_url} not found\n'
