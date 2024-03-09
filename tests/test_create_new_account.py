import pytest
import allure


@allure.feature('Test ui')
@allure.story('Test create account')
@allure.title('Test create new account with all correct fields')
@allure.severity(allure.severity_level.CRITICAL)
def test_create_new_account_with_all_correct_fields(create_account, start_end):
    create_account.open_page()
    create_account.fill_all_form()
    create_account.check_alert_text('Thank you for registering with Main Website Store.')


@allure.feature('Test ui')
@allure.story('Test create account with old account')
@allure.title('Test create create account with old account')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_create_account_with_old_account(create_account, create_new_account, start_end):
    old_data = create_new_account
    create_account.open_page(delete_cookies='Yes')
    create_account.fill_all_form(old_data)
    create_account.check_alert_text(
        'There is already an account with this email address. '
        'If you are sure that it is your email address, click here to get your password and access your account.'
    )

# def test_create_account_with_incorrect_email(create_account):