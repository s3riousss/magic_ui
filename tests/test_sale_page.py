import allure
import pytest


@allure.story('Test redirect to show women details')
@allure.title('Test redirect to page "show women details"')
@pytest.mark.smoke
def test_show_women_details(sale_page, start_end, set_allure):
    sale_page.open_page()
    sale_page.check_click_button_url_women()


@allure.story('Test redirect to men bargains')
@allure.title('Test redirect to page "men bargains"')
@pytest.mark.smoke
def test_men_bargains(sale_page, start_end, set_allure):
    sale_page.open_page()
    sale_page.check_men_bargains()


@allure.story('Test correct teext in block luma great steal')
@allure.title('Test luma great steal"')
@pytest.mark.regression
def test_luma_great_steal(sale_page, start_end, set_allure):
    sale_page.open_page()
    sale_page.luma_gear_steals()
    sale_page.check_title(exp_title='Luma Gear Steals')
    sale_page.check_info(exp_info='Your best efforts deserve a deal')
    sale_page.check_more_icon(exp_more_icon='Shop Luma Gear')
