import allure
import pytest


@pytest.fixture()
def set_allure():
    allure.dynamic.feature('Test ui')
    allure.dynamic.severity(allure.severity_level.CRITICAL)
