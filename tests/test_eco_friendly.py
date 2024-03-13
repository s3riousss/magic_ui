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


@allure.feature('Test ui')
@allure.story('Test add to cart without options')
@allure.title('Test add to cart without options')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_to_cart_without_options(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.add_to_cart()
    eco_friendly.check_alert_text('You need to choose options for your item.')


# probably next version will be use
# def test_check_chose_color_white_and_size(eco_friendly):
#     eco_friendly.open_page()
#     eco_friendly.choose_color('White')
#     eco_friendly.add_to_cart()