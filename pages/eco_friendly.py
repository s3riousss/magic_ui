from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'
    find_item = None

    def select_sort(self, value):
        selected = self.find(loc.sort)
        actions = ActionChains(self.driver)
        actions.move_to_element(selected).click().perform()
        self.wait_full_to_load()
        dropdown = Select(selected)
        dropdown.select_by_value(value)
        self.wait_full_to_load()
        items = self.find_all(loc.product)
        list_exp = []
        match value:
            case 'price':
                for price in items:
                    list_exp.append(float(price.find_element(*loc.price).text.replace('$', '')))
                self.assert_check(list_exp, sorted(list_exp), f'Error sorted {value}')
            case 'name':
                for name in items:
                    list_exp.append(name.find_element(*loc.product_name).text)
                self.assert_check(list_exp, sorted(list_exp), f'Error sorted {value}')
        print(list_exp)

    def add_to_cart(self):
        self.wait_full_to_load()
        actions = ActionChains(self.driver)
        if self.find_item:
            add_to_cart = self.find_item.find_element(*loc.add_to_cart)
            actions.move_to_element(self.find_item)
        else:
            find_item = self.find_all(loc.product_details)[0]
            add_to_cart = find_item.find_element(*loc.add_to_cart)
            actions.move_to_element(find_item)
        actions.move_to_element(add_to_cart)
        actions.click()
        actions.perform()
        self.screenshot()
