from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils.project_ec import text_is_not_empty_in_element
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
        WebDriverWait(self.driver, 5).until(text_is_not_empty_in_element(loc.welcome))
        dropdown = Select(selected)
        dropdown.select_by_value(value)
        WebDriverWait(self.driver, 5).until(text_is_not_empty_in_element(loc.welcome))
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

# currently unused
    def choose_color(self, color):
        WebDriverWait(self.driver, 5).until(text_is_not_empty_in_element(loc.welcome))
        self.find_item = self.driver.find_elements(*loc.product_details)[0]
        color_chose = self.find_item.find_element(By.CSS_SELECTOR, f'[option-label="{color}"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(self.find_item)
        actions.move_to_element(color_chose)
        actions.click()
        actions.perform()

    def add_to_cart(self):
        WebDriverWait(self.driver, 5).until(text_is_not_empty_in_element(loc.welcome))
        actions = ActionChains(self.driver)
        if self.find_item:
            add_to_cart = self.find_item.find_element(*loc.add_to_cart)
            actions.move_to_element(self.find_item)
        else:
            find_item = self.driver.find_elements(*loc.product_details)[0]
            add_to_cart = find_item.find_element(*loc.add_to_cart)
            actions.move_to_element(find_item)
        actions.move_to_element(add_to_cart)
        actions.click()
        actions.perform()
