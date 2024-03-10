import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base_page import BasePage
from pages.locators import eco_friendly_locators as loc
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'


    def select_sort(self, value):
        selected = self.find(loc.sort)
        actions = ActionChains(self.driver)
        actions.move_to_element(selected).click().perform()
        time.sleep(1)
        dropdown = Select(selected)
        dropdown.select_by_value(value)
        time.sleep(1)
        # WebDriverWait(self.driver, 5).until(ec.url_contains(f'product_list_order={value}'))
        # self.wait_element_presence(5, loc.product)
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

    # def choose_size(self):
    #     WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.ID, "layered-filter-block")))
    #     size_title = self.driver.find_elements(By.CLASS_NAME, "filter-options-title")[2]
    #     actions = ActionChains(self.driver)
    #     actions.move_to_element(size_title).click().perform()
    #     # WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[data-role='title'][aria-selected='true']")))
    #
    #
    #     # Найти и кликнуть на элемент "XS"
    #     xs_size = self.driver.find_elements(By.CSS_SELECTOR, "div.swatch-option.text[option-label='XS']")[0]
    #     xs_size.click()


