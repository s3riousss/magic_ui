import allure


@allure.feature('Test ui')
@allure.story('Test sort by price')
@allure.title('Test sort by price')
@allure.severity(allure.severity_level.CRITICAL)
def test_sorted_by_price(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.select_sort('price')


@allure.feature('Test ui')
@allure.story('Test sort by name')
@allure.title('Test sort by name')
@allure.severity(allure.severity_level.CRITICAL)
def test_sorted_by_name(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.select_sort('name')


def test_check_now_shopping_by_size_xs(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.choose_size()
